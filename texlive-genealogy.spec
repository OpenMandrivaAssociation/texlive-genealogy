# revision 15878
# category Package
# catalog-ctan /fonts/genealogy
# catalog-date 2007-10-01 22:41:52 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-genealogy
Version:	20071001
Release:	2
Summary:	A compilation genealogy font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/genealogy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A simple compilation of the genealogical symbols found in the
wasy and gen fonts, essentially adding the male and female
symbols to Knuth's 'gen' font, and so avoiding loading two
fonts when you need only genealogical symbols. The font is
distributed as MetaFont source.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/genealogy/drgen.mf
%{_texmfdistdir}/fonts/source/public/genealogy/drgen10.mf
%{_texmfdistdir}/fonts/tfm/public/genealogy/drgen10.tfm
%doc %{_texmfdistdir}/doc/fonts/genealogy/README
%doc %{_texmfdistdir}/doc/fonts/genealogy/licence.txt
%doc %{_texmfdistdir}/doc/fonts/genealogy/testgen.dvi
%doc %{_texmfdistdir}/doc/fonts/genealogy/testgen.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
