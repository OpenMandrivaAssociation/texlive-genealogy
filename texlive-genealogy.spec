%global tl_name genealogy
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A compilation genealogy font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/genealogy
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A simple compilation of the genealogical symbols found in the wasy and
gen fonts, adding the male and female symbols to Knuth's 'gen' font, and
so avoiding loading two fonts when you need only genealogical symbols.
The font is distributed as Metafont source.

