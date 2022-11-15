Name:		texlive-bigintcalc
Version:	53172
Release:	1
Summary:	Integer calculations on very large numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bigintcalc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigintcalc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigintcalc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigintcalc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides expandable arithmetic operations with big
integers that can exceed TeX's number limits.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bigintcalc
%{_texmfdistdir}/tex/generic/bigintcalc
%doc %{_texmfdistdir}/doc/latex/bigintcalc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
