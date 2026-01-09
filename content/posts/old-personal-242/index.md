---
title: "Greasemonkey tegen Blackboard"
date: 2005-04-23T16:01:00
author: alper
categories:
  - nederlands
  - delft
  - software-engineering
  - internet
---

Het [Blackboard](http://blackboard.tudelft.nl) Course Information system wat we hier op de TU gebruiken werkt best aardig. Een langlopende irritatie is dat het inloggen niet automatisch kan en je elke keer een wachtwoord in moet voeren.

De inlogprocedure is ook nog eens ontzettend paranoïde en compleet tevergeefs nu ik goed naar kijk. Het volgende stuk code regelt het valideren van het inlogformulier:

```
var _useChallenge = false;

function validate_form(form) {

if ( form.user_id.value == "" || form.password.value == "" ) {

alert( "Please enter a username and password." );

return false;

}

//short-cut if challenge/response is disabled.

if ( !_useChallenge ) {

form.encoded_pw.value = base64encode( form.password.value );

form.password.value =  "";

return true;

}

var passwd_enc = calcMD5(form.password.value);

var final_to_encode = passwd_enc + form.one_time_token.value;

form.encoded_pw.value = calcMD5(final_to_encode);

form.password.value = "";

return true;

}
```

Het is ten eerste een redelijk raadsel waarom ze het op deze manier doen en niet gewoon een beveiligde (https) verbinding gebruiken. Maar het stuk code hierboven zou best wel veilig zijn als `_useChallenge` aan stond en ze die *one_time_token* gebruikten. Nu gaat het wachtwoord toch weer redelijk plat naar de server.

Maar genoeg geneuzel, als je je gebruikersnaam en wachtwoord invult in het volgende [Greasemonkey](http://greasemonkey.mozdev.org/)-script: [blackboardLogin.user.js](http://www.alper.nl/ajax/blackboardLogin.user.js), vlieg je automatisch door de inlogpagina heen.