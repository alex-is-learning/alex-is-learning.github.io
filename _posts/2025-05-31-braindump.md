---
layout: post
title: "Adding functionality to the Arch Linux laptop" 
date: 2025-05-31 17:26
published: true 
# slug: "optional-custom-slug"      

# Syntax reminder: 
# [link text](url)
# ![alt text](/path/to/image.jpg)
---

## Daily post hello world
I'm not sure what I'm going to write about yet. Let's see...

I published the first of my "shame" series, inspired by my friend Delia,
yesterday (to my substack). I love how much of a non-event it feels like. I
feel, with this and with finally hearing back re: the work trial I did (after 23
days), suddenly very light and free. It's the weekend too -- even though I'm
unemployed so weekends don't really mean anything, they still feel very real,
and I like preserving them as non-main-work days.

It's 5pm already somehow, I don't know where the hell the day went. I watched a
John Vervaeke talk in the morning (him at at a conference organised by a
philosophy AI app that he endorses - I forget the name but I've downloaded it
and had a 6-minute call with an AI version of a Greek Philosopher today. I'm
excited to use it more -- I take a Vervaeke cosign very seriously, I think he is
a brilliant man).

I've spent a big chunk of time tweaking my Arch Linux laptop (did I mention I
use Arch Linux?). I've had a few instances now where I write a blog post on my
Arch laptop, and because it's so incredibly basic (by personal design!), I can't
access relevant links, so once I've pushed the changes via git, I have to
remember to edit the code from my Macbook, so I can add links. This is silly
because no one will read this, but also because it's redundant, so now I've made
my Arch laptop more elaborate.

## Adding functionality to the laptop

As of this morning, all this beautiful 13 year old hunk of plastic had on it was
the Linux TTY (I forget what it stands for but basically, a barebones terminal),
and git. 

Now I have an actual desktop setup, the i3 Window/workspace manager, firefox so
I can get to links if I need to e.g. grab a link to a blog post by someone else,
and Obsidian. I may remove Obsidian if it poses a distraction, but I figure it
might be nice, maybe, to be able to access my notes. I'm wary of Sasha Chapin's
[Notes Against Note-Taking
Systems](https://sashachapin.substack.com/p/notes-against-note-taking-systems)
here - I don't want Obsidian to distract me and detract from the beautiful
turbo-basic setup I had this morning. So we'll see.

Oh god, currently I can't copy-paste from Firefox (e.g. the URL for that Sasha
post) into this Neovim instance in Alacritty. Let's see what AI has to say about
this...

Ok, time to peace-out from Neovim and install some shit. Gimme 5...

Ok, I'm back.

Ok look, I admit it. Arch Linux is an absolute pain. I just had to spend 10
minutes installing a package and tweaking some config files to make it the case
that I can copy-paste from an app (like Firefox) into Neovim. I think if I was
trying this out a few years ago, before AI, I may have thrown in the towel. But
now AI is here and it's totally fine and actually fun to do, if you don't mind
the setup cost. 

## I can now talk to Gemini 2.5 from my Arch Linux laptop 
Now I have i3, I can actually open apps other than the command line, which is
exciting (for me -- I really hope no one is reading this, lol). 

This still feels like a nice stripped-down laptop. Sure, I can browse the
internet now, but it's relatively slow, the screen is small, the trackpad is
abysmal. I could learn Vimium to browse Firefox without having to use the
trackpad (or the famous ThinkPad nipple), but... I imagine the slow speed will
keep me using this as a "90% neovim, 10% searching for links/checking my github
build" machine. Nice and simple, still. 

## MathAcademy
I want to do a big chunk of MathAcademy.com today. I have my beeminder goal set
to 15 mins of MA per day, but I'd like to do maybe 1 hour today. It has me
working through very embarrassingly easy prealgebra, because I did so badly on
the placement exam. 90% if stuff that I vaguely remember learning and can just
intuit, 10% is stuff that I've forgotten or never touched. So it feels pretty
damn inefficient, like they're making me do a huge amount of stuff that I can
just intuit, but I definitely see the value in making sure I have 100% of these
foundations in place before progressing. It's going to be absolutely ages before
I'm doing anything actually useful... I have a vague sense that maths is an
important thing that I missed out on, that maybe linear algebra or calculus will
help me understand the world better, somehow... we'll see. Will I stick to it
long enough to see benefits? I hope so. But I'm definitely doing far too much
right now. 
 
## Why do I care about this stuff? 
I find this laptop to be wildly charming. Especially when it was literally just
the terminal (TTY) and vim. I just absolutely love the "basic as hell terminal
from the 1960s/1970s/1980s" aesthetic -- it's so insanely vibe-y to me. I think
it's partially from playing Fallout 3 as a teenager -- in that game, you'd have
to "hack" computers sometimes (an actually truly pathetic mini-game involving
guessing the right word via pattern matching, a kind of proto-wordle), and the
computers in the game had the iconic black and green terminal theme. Also I
remember in Call of Duty Black Ops (this memory has literally just come back to
me now after probably 12 years!!) -- there was an easter egg where, in the main
menu, you have the POV of someone strapped to a chair, a prisoner of war, and if
you spammed the shoulder buttons on your controller you'd break out of the
chair, and you could explore the room you were in, and you could go over to a
computer terminal and play the game... I forget what it's called, but it's an
old-school text based game where it says like "you are in a room, you can see
xyz, what do you do" and you try out different typed commands like "leave room"
or "open box" and that's the game. There was a Hitchhiker's Guide to the Galaxy
one and it was actually super fun playing a game that engaged your imagination
so much. Anyway, what was I talking about? 

Oh yeah, so I don't know, for whatever reason, the act of interfacing with a
computer in a very barebones way (i.e. the terminal) just feels sick to me. I
think, in addition to the aesthetic of it, the nerdiness that I for whatever
reason find appealing, there's also the sense of mastery, of arcane knowledge.
Of making your family's brains boggle at what the fuck you're doing, what kind
of wizardry is this? I shocked my sister yesterday by telling her that Netflix
is made of code (my family are deeply tech illiterate). A large part of my
identity, especially as a kid, came from being smart, the gifted one, so I do
think there's an echo of that in learning stuff that I know is niche and arcane
and special. 

There's also just a very very clear sense of progression and learning in
programming. It's one of the most concrete places (probably maths is similar),
where you can be like "wow, I knew nothing about xyz a week ago, and now look at
me". Be that a programming language, Linux terminal commands, a key Obsidian
community plugin, extensible open source software, creative software like
Ableton/Photoshop/Final Cut Pro. Computers just give you this incredible flow
state experience, a very tight coupling to the "environment" (which is key to
flow, John Vervaeke uses the example of rock climbing). Very clear feedback
loops, very clear progression. And this is why video games are so compelling -
they take this stuff and put it on steroids, as they're not hard work (mostly)
-- you can totally hit a wall with programming, but a game like DOOM Eternal or
Call of Duty is designed to keep you in flow. (It's funny how talking about Call
of Duty makes me feel like a boomer - do people still play it? I imagine it has
been supplanted by Fortnite/Apex Legends etc). 

Anyway, my point is - computers are cool. I wonder if I should have done a
computer science degree -- I have a friend who told me that we are considered
the "lost generation", because computer programming was briefly removed from the
curriculum in English schools when we were attending them, so that we didn't get
exposed to programming in a reliable way. I think if we'd had coding at school I
would have loved it - when I finally had my first coding-based assignment
(during my Masters, in MatLab, I loved it but go an incredibly poor score
because I completely missed what functions were about so ended up with insane
copy-pasted code instead of using functions, lmao). And I thought myself Python
and SQL and got a job as a data analyst (as did my 3 friends from school who all
did Physics degrees - they're still data analysts now. One of them asked me
recently if I'd ever return -- I love coding, and I'd love to learn proper
software engineering, I keep hearing the siren call of Rust, but I definitely
won't be a data analyst again.

Ok so anyway. this is great - I have obsidian open in my second i3 workspace,
Firefox in workspace 3, but this still feels like a very pure writing
experience. Good stuff. I love this setup so much!!!
