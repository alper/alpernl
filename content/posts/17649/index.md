---
author: alper
categories:
  - english
  - internet
  - software-engineering
date: "2024-11-03T14:55:25+00:00"
title: MySQL encoding mistakes corrupting data in this decade?!?
aliases:
  - /dingen/2024/11/17649/

---
Turns out I hadn't noticed my hosting provider [Vimexx](https://www.vimexx.nl) has their MySQL databases on `latin1` coding and this blog was running on that happily corrupting data.

Given how common an occurrence this is—MySQL very regularly will throw your shit into the street and set fire to it—I had expected there being scripts or resources to fix this. Of course nothing was to be found anywhere.

I asked [the Mastodon MySQL expert](https://infosec.exchange/@isotopp) who did have a resource on the exact problem: [https://blog.koehntopp.info/2020/08/18/mysql-character-sets.html](https://blog.koehntopp.info/2020/08/18/mysql-character-sets.html)

The way I fixed it was a bit more manual than I'd have liked but where I got is good enough and I'm not sure I'll go for anything perfect:

Go to the phpMyAdmin and audit all the database tables.

{{< figure src="CleanShot-2024-11-03-at-16.05.26@2x.png" alt="" caption="" >}}

My tables are in a mix of InnoDB and MyISAM which seems to be weird but not really problematic. I also had some [Yoast](https://yoast.com) tables that were lingering there which I dropped.

Find the setting and convert all tables and their columns to the collation `utf8mb4_unicode_ci`. A collation implies the `utf8mb4` character set that is its prefix so you don't have to change the character set.

Now all your stuff is in UTF-8 but because of a coding error a lot of your content is messed up. A unicode character can be more than one byte but in latin1 each character can only be a single byte. So if your unicode character is two bytes, they are interpreted as two `latin1` characters which is why you end up with stuff like " **Ã®**".

Maybe there would have been a clean automatic way to convert the data, but I felt it was fiddly enough as it was, so I opted for a manual fix. I identified where the corruption happened:

- `wp_posts` columns `post_content` and `post_title`
- `wp_comments` column `comment_content`
- `wp_usermeta` column `meta_value`

Then I just ran queries to fix all the mismatches:

ü → ü  
Ãœ → Ü  
é → é  
Ã‰ → É  
ğ → ğ  
Ç → Ç  
etc.

Luckily in almost all cases the wrong coded string is unique and can simply be replaced with the right character.

Check if a string is in the column:  
`SELECT post_content from wp_posts where post_content LIKE BINARY '%Ç%' and post_status='publish'`

Later on check for specific characters and their environment in what can be very long post bodies:  
`SELECT SUBSTRING(post_content, LOCATE('Ã', post_content)-15, 40), post_content from wp_posts where post_content LIKE BINARY '%Ã%' and post_status='publish'`

Replace the wrong string sequence with the correct character:  
`UPDATE wp_posts SET post_content = REPLACE(post_content, 'Ç', 'Ç') WHERE INSTR(post_content, 'Ç') > 0`

After some hours of auditing and pounding SQL most of the things should be fixed and whatever's left I can live with.

## Conclusion

The moral of this story is that the entire complex of Wordpress/PHP/MySQL is a pile of shit that should be burnt off the face of the planet. The fact that we can have these kind of encoding issues in the year 2024 shows what an absolute joke these systems are. Especially with the Mullenweg meltdowns, anybody who can get out of Wordpress should do so.

This blog hasn't received a comment or other bit of interactivity in years so I think I could also rip all the content (effectively just two columns in `wp_posts`) out and host it on something that's statically built. No reason to pay for a shit hosting provider like Vimexx anymore either.
