Name:           neverhood
Version:        1
Release:        1%{?dist}
Summary:        1996 point-and-click adventure claymation game
License:        Proprietary
URL:            http://www.neverhood.se/

Source0:        Neverhood.iso
Source1:        %{name}
Source2:        %{name}.ini
Source3:        %{name}.desktop

BuildArch:      noarch

BuildRequires:  /usr/bin/convert
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/dos2unix
BuildRequires:  /usr/bin/iconv
BuildRequires:  /usr/bin/7z

Requires:       scummvm
Requires:       python3-appdirs
Requires:       python3 >= 3.6

%description
The Neverhood (also called The Neverhood Chronicles, released in Japan as
Klaymen Klaymen) is a 1996 point-and-click adventure game developed by
The Neverhood, Inc. and published by DreamWorks Interactive. The game follows
the adventure of a claymation character named Klaymen as he discovers his
origins and his purpose in a world made entirely out of clay. When the game
was originally released, it was unique in that it featured all of its animation
done entirely in claymation, including all of the sets, rather than 2- or
3-dimensional computer graphics, like many other games at its time. The
gameplay consists mostly of the player guiding the main character Klaymen
around and solving puzzles to advance in the game. As the player advances
through different areas of the game, there are various video sequences that
help advance the plot. In addition to being unique, The Neverhood aimed at
being quirky and humorous, as is evident by the characters, the music, and
the plot sequence of the game.

This package uses the ScummVM program to run the game using the original data
files.


%prep
%setup -Tc
7z x %{SOURCE0}
dos2unix readme.txt
iconv -f cp850 -t utf-8 readme.txt -o readme.txt


%build
for res in 16 32 48; do
  mkdir -p hicolor/${res}x${res}/apps
done
cd hicolor
convert ../*.ico %{name}.png
mv %{name}-3.png 16x16/apps/%{name}.png
mv %{name}-4.png 32x32/apps/%{name}.png
mv %{name}-5.png 48x48/apps/%{name}.png
rm %{name}-*.png
cd -


%install
mkdir -p %{buildroot}%{_datadir}/games/%{name}/DATA
install -m 644 DATA/*.blb %{buildroot}%{_datadir}/games/%{name}/DATA/

install -Dm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

install -Dm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/%{name}.ini

desktop-file-install --dir %{buildroot}%{_datadir}/applications/ %{SOURCE3}

mkdir -p %{buildroot}%{_datadir}/icons
cp -r hicolor %{buildroot}%{_datadir}/icons


%check
for RES in $(ls hicolor); do
  file hicolor/$RES/apps/%{name}.png | grep "$(echo $RES | sed 's/x/ x /')"
done


%files
%doc readme.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%config(noreplace) %{_sysconfdir}/xdg/%{name}.ini
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/DATA
%{_datadir}/games/%{name}/DATA/*.blb

%changelog
* Wed Aug 23 2017 Miro Hrončok <mhroncok@redhat.com> - 1-1
- Initial package

