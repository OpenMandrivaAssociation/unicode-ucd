Name:           unicode-ucd
Version:        13.0.0
Release:        1
Summary:        Unicode Character Database
Group:          System/Internationalization
License:        MIT
URL:            http://www.unicode.org/ucd/
Source0:        http://www.unicode.org/Public/zipped/%{version}/UCD.zip#/UCD-%{version}.zip
Source1:        http://www.unicode.org/Public/zipped/%{version}/Unihan.zip#/Unihan-%{version}.zip
# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source2:       http://www.unicode.org/copyright.html#/copyright.html
Source3:        http://www.unicode.org/Public/zipped/%{version}/ReadMe.txt
BuildArch:      noarch

%description
The Unicode Character Database (UCD) consists of a number of data files
listing Unicode character properties and related data. It also includes
data files containing test data for conformance to several important
Unicode algorithms.

%prep
%setup -q -c
grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)
cp %{S:2} copyright.html
cp %{S:1} Unihan.zip
cp %{S:3} ReadMe.txt

%build
# Nothing to do here

%install
install -d %{buildroot}%{_datadir}/unicode/ucd
cp -ar . %{buildroot}%{_datadir}/unicode/ucd

%files
%doc ReadMe.txt copyright.html
%dir %{_datadir}/unicode
%{_datadir}/unicode/ucd/
