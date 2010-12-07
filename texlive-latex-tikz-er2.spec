%define shortname tikz-er2
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Tikz-er2 is a LaTeX package to draw Entity-Relationship diagrams
Summary(hu.UTF-8):	Tikz-er2 egy LaTeX-csomag entitás-kapcsolat diagramokhoz
Name:		texlive-latex-%{shortname}
Version:	20100402
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://home.dei.polimi.it/mredaelli/circuitikz/index.html
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{shortname}-%{version}.tar.xz
# Source0-md5:	89b499718897a71ade7786b385439b6f
Requires(post,postun):	/usr/bin/texhash
Requires:	texlive-latex
Requires:	texlive-latex-pgf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tikz-er2 is a LaTeX package to draw Entity-Relationship diagrams.

%description -l hu.UTF-8
Tikz-er2 egy LaTeX-csomag entitás-kapcsolat diagramokhoz.

%prep
%setup -q -n %{shortname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/texmf-dist/tex/latex/%{shortname}
install %{shortname}.sty $RPM_BUILD_ROOT%{_datadir}/texmf-dist/tex/latex/%{shortname}

install -d $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/%{shortname}
install docs/* $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc %{_datadir}/texmf-dist/doc/latex/%{shortname}
%{_datadir}/texmf-dist/tex/latex/%{shortname}
