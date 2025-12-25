---
_last_editor_used_jetpack: block-editor
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
date: "2022-02-19T20:07:00+00:00"
guid: https://alper.nl/dingen/?p=16709
parent_post_id: null
post_id: "16709"
title: Learning about Rust types and dynamic dispatch
aliases:
  - /dingen/2022/02/learning-about-rust-types-and-dynamic-dispatch/

---
So I had some code very similar to the following that wouldn't compile and me with my old Python head was a bit surprised why this was the case. It was a bit more complicated to figure it out in my example but this simplified version makes it pretty clear.

```
trait SomeTrait {}

impl SomeTrait for u8 {}
impl SomeTrait for u16 {}

fn function() -> impl SomeTrait {
    if true {
        0u8
    } else {
        0u16
    }
}
```

Why did I think it would work? Because both types implement the same trait, it'll come down to the same thing in the end and that should be fine, right? I think that's Python talking.

> The Rust compiler needs to know how much space every function's return type requires.
>
> https://doc.rust-lang.org/rust-by-example/trait/dyn.html

Let's think about it from a Rust perspective which means think about the memory layout of this. We're on the stack here and in this case it may only be a difference of a byte, it's very possible to have two vastly different types implement the same trait. That can't possibly work.

The answer then of course is to:  
1\. Move things into the heap with \`Box. That doesn't fully solve it because then both arms have a different type `Box<u8>` and `Box<u16>` respectively. But crucially now they're always the same size.  
2\. Change the return type to a trait object that both types conform to with `dyn`.

```
trait SomeTrait {}

impl SomeTrait for u8 {}
impl SomeTrait for u16 {}

fn function() -> Box<dyn SomeTrait> {
    if true {
        Box::new(0u8)
    } else {
        Box::new(0u16)
    }
}
```

This works and is [dispatched dynamically](https://doc.rust-lang.org/book/ch17-02-trait-objects.html#trait-objects-perform-dynamic-dispatch).

Thanks by the way to the people in the [Tokio](https://tokio.rs) Discord for being extremely patient with me.
