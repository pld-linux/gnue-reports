Summary:	GNUe Reports - a platform and output-independent reporting system
Summary(pl):	GNUe Reports - niezale¿ny od platformy i wyj¶cia system raportów
Name:		gnue-reports
Version:	0.1.7
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.gnuenterprise.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	226923ede11b9b69508ed82bd68f72a8
URL:		http://www.gnuenterprise.org/
BuildRequires:	gnue-common
BuildRequires:	python
BuildRequires:	python-devel
Requires:	gnue-common
Requires:	pysablot
Requires:	python
Obsoletes:	GNUe-Reports
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUe Reports is a platform and output-independent reporting
system. It reads an XML-based report definition and generates
arbitrary XML output that can further be translated into any format
for which there is an adapter. GNUe Reports currently has outputs
for Text, HTML, Label Stock, and CSV -- with PDF, Postscript, and
Gnumeric/Excel formats in the works. Reports can output directly to
a file, as an email attachment, to a printer, or to a HylaFax server.

%description -l pl
GNUe Reports to niezale¿ny od platformy i wyj¶cia system raportów.
Czyta definicjê raportu opart± na XML-u i generuje dowolne wyj¶cie
XML, któ}re nastêpnie mo¿e byæ przet³umaczone na dowolny format, dla
którego istnieje adapter. GNUe Reports aktualnie ma wyj¶cia do tekstu,
HTML-a, formatu Label Stock oraz CSV - z formatami PDF, Postscript i
Gnumeric/Excel w trakcie tworzenia. Reports mo¿e generowaæ wyj¶cie
bezpo¶rednio do pliku, jako za³±cznik e-maila, na drukarkê lub do
serwera HylaFax.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO doc/*.* doc/technotes
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/gnue/reports
%{_datadir}/gnue/filters
%{_datadir}/gnue/grpc/*
%{_mandir}/man?/*
