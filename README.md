The Neverhood RPM for Fedora (unofficial, nonfree)
==================================================

How to build
------------

 1. get `Neverhood.iso`, place it in this folder
 2. run `fedpkg --release f26 --module-name neverhood mockbuild` or similar
 3. install resulting RPM (from `results_neverhood/`)

Using
-----

There is an app launcher called *The Neverhood*. Or you can run `neverhood`
from the console. It forwards all arbitrary options to `scummvm`, see them with
`neverhood --help`. Such option my be `--no-fullscreen`.

There is a config file in `/etc/xdg/neverhood.ini` that is copied to
`~/.config/neverhood.ini` if that one is not present. Feel free to tweak the
options in your config, such as setting `skiphallofrecordsscenes` to `true`
or `fullscreen` to `false`.

Enjoy.

![Illustrative pic](http://neverhood.etomite.sk/imgs/galcredits/large/credit17.jpg)


License
-------

The Neverhood is:

> © & ℗ 1995 - 1996 Microsoft Corporation. All rights reserved.
>
> © & ℗ 1996 DreamWorks Interactive L.L.C. All rights reserved.
>
> Warning: This computer program is protected by copyright
> law and international treaties. Unauthorized reproduction or
> distribution of this program, or any portion of it, may result in
> severe civil and criminal penalties, and will be prosecuted
> to the maximum extent possible under the law.
>
> "The Neverhood" is a registered trademark of the Neverhood.
>
> "DreamWorks Interactive" is a trademark of DreamWorks L.L.C.

The files in this repository are Public Domain.
