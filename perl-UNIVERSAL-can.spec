#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UNIVERSAL
%define	pnam	can
Summary:	UNIVERSAL::can - Hack around people calling UNIVERSAL::can() as a function
Summary(pl.UTF-8):	UNIVERSAL::can - poprawianie ludzi wywołujących UNIVERSAL::can() jako funkcję
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

%description -l pl.UTF-8
Klasa UNIVERSAL udostępnia kilka domyślnych metod, które mogą być
używane przez wszystkie obiekty. Zorientowanie obiektowe pozwala
programistom przykryć te metody w podklasach, aby zapewnić bardziej
konkretne i odpowiednie zachowanie.

Niektórzy autorzy wywołują metody w klasie UNIVERSAL na potencjalnych
wywołujących jako funkcje, pomijając jakiekolwiek przykrywanie. Jest
to niedobre i nie należy tego robić. Niestety nie każdy zwraca uwagę
na to ostrzeżenie i jego zły kod może zepsuć inny dobry kod.

Na szczęście ten moduł zastępuje UNIVERSAL::can() metodą sprawdzającą
czy pierwszy argument jest poprawnym wywołującym (obiektem -
pobłogosławioną referencją - albo nazwą klasy). Jeśli tak, a klasa
wywołującego ma własną metodę can(), wywołuje ją jako metodę. W
przeciwnym wypadku wszystko działa tak, jak można by się tego
spodziewać.

Jeśli ktoś próbuje wywołać UNIVERSAL::can() jako funkcję, ten moduł
wygeneruje ostrzeżenie słowne (perllexwarn). Można wyłączyć je - ale
nie należy tego robić, zamiast tego lepiej poprawić kod.

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
