#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UNIVERSAL
%define	pnam	can
Summary:	UNIVERSAL::can - Hack around people calling UNIVERSAL::can() as a function
Summary(pl):	UNIVERSAL::can - poprawianie ludzi wywo³uj±cych UNIVERSAL::can() jako funkcjê
Name:		perl-UNIVERSAL-can
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4386c4f7479447fc5b51e8c3770cd2f4
URL:		http://search.cpan.org/dist/UNIVERSAL-can/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.60
BuildRequires:	perl-Test-Warn >= 0.08
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The UNIVERSAL class provides a few default methods so that all objects
can use them. Object orientation allows programmers to override these
methods in subclasses to provide more specific and appropriate
behavior.

Some authors call methods in the UNIVERSAL class on potential
invocants as functions, bypassing any possible overriding. This is
wrong and you should not do it. Unfortunately, not everyone heeds this
warning and their bad code can break your good code.

Fortunately, this module replaces UNIVERSAL::can() with a method that
checks to see if the first argument is a valid invocant (whether an
object - a blessed referent - or the name of a class). If so, and if
the invocant's class has its own can() method, it calls that as a
method. Otherwise, everything works as you might expect.

If someone attempts to call UNIVERSAL::can() as a function, this
module will emit a lexical warning (see perllexwarn) to that effect.
You can disable it with no warnings; or no warnings 'UNIVERSAL::isa';,
but don't do that; fix the code instead.

%description -l pl
Klasa UNIVERSAL udostêpnia kilka domy¶lnych metod, które mog± byæ
u¿ywane przez wszystkie obiekty. Zorientowanie obiektowe pozwala
programistom przykryæ te metody w podklasach, aby zapewniæ bardziej
konkretne i odpowiednie zachowanie.

Niektórzy autorzy wywo³uj± metody w klasie UNIVERSAL na potencjalnych
wywo³uj±cych jako funkcje, pomijaj±c jakiekolwiek przykrywanie. Jest
to niedobre i nie nale¿y tego robiæ. Niestety nie ka¿dy zwraca uwagê
na to ostrze¿enie i jego z³y kod mo¿e zepsuæ inny dobry kod.

Na szczê¶cie ten modu³ zastêpuje UNIVERSAL::can() metod± sprawdzaj±c±
czy pierwszy argument jest poprawnym wywo³uj±cym (obiektem -
pob³ogos³awion± referencj± - albo nazw± klasy). Je¶li tak, a klasa
wywo³uj±cego ma w³asn± metodê can(), wywo³uje j± jako metodê. W
przeciwnym wypadku wszystko dzia³a tak, jak mo¿na by siê tego
spodziewaæ.

Je¶li kto¶ próbuje wywo³aæ UNIVERSAL::can() jako funkcjê, ten modu³
wygeneruje ostrze¿enie s³owne (perllexwarn). Mo¿na wy³±czyæ je - ale
nie nale¿y tego robiæ, zamiast tego lepiej poprawiæ kod.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/*.pm
%{_mandir}/man3/*
