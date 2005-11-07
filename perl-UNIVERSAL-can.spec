#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UNIVERSAL
%define	pnam	can
Summary:	UNIVERSAL::can - Hack around people calling UNIVERSAL::can() as a function
#Summary(pl):	
Name:		perl-UNIVERSAL-can
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40cea820351a759f293af68115452ef7
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
The UNIVERSAL class provides a few default methods so that all objects can use
them.  Object orientation allows programmers to override these methods in
subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants as
functions, bypassing any possible overriding.  This is wrong and you should not
do it.  Unfortunately, not everyone heeds this warning and their bad code can
break your good code.

Fortunately, this module replaces UNIVERSAL::can() with a method that checks
to see if the first argument is a valid invocant (whether an object -- a
blessed referent -- or the name of a class).  If so, and if the invocant's
class has its own can() method, it calls that as a method.  Otherwise,
everything works as you might expect.

If someone attempts to call UNIVERSAL::can() as a function, this module will
emit a lexical warning (see perllexwarn) to that effect.  You can disable it
with no warnings; or no warnings 'UNIVERSAL::isa';, but don't do that;
fix the code instead.

# %description -l pl
# TODO

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
