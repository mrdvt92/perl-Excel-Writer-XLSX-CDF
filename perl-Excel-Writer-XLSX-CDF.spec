Name:           perl-Excel-Writer-XLSX-CDF
Version:        0.03
Release:        1%{?dist}
Summary:        Generates Excel Document with Continuous Distribution Function Chart
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Excel-Writer-XLSX-CDF/
Source0:        http://www.cpan.org/modules/by-module/Excel/Excel-Writer-XLSX-CDF-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Excel::Writer::XLSX)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Round::SignificantFigures)
BuildRequires:  perl(Package::New)
Requires:       perl(DateTime)
Requires:       perl(Excel::Writer::XLSX)
Requires:       perl(File::Temp)
Requires:       perl(List::MoreUtils)
Requires:       perl(List::Util)
Requires:       perl(Math::Round::SignificantFigures)
Requires:       perl(Package::New)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Generates Excel Document with Continuous Distribution Function Chart from
the supplied data.

%prep
%setup -q -n Excel-Writer-XLSX-CDF-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 07 2022 Michael R. Davis <mrdvt92@yahoo.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
