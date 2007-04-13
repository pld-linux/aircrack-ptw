# TODO: optflags
Summary:	Faster then aircrack-ng WEP key cracker
Summary(pl.UTF-8):	Szybszy niż aircrack-ng łamacz kluczy WEP
Name:		aircrack-ptw
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.cdc.informatik.tu-darmstadt.de/aircrack-ptw/download/%{name}-%{version}.tar.gz
# Source0-md5:	1d7d84d1e69189bc1397db3f565c183a
URL:		http://www.cdc.informatik.tu-darmstadt.de/aircrack-ptw/
BuildRequires:	libpcap-devel
Requires:	aircrack-ng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Using this version, it is possible to recover a 104 bit WEP key with
probability 50% using just 40,000 captured packets. For 60,000
available data packets, the success probability is about 80% and for
85,000 data packets about 95%.

%description -l pl.UTF-8
Używając tego oprogramowania istnieje możliwość odzyskania
104-bitowego klucza WEP z prawdopodobieństwem 50% przy wykorzystaniu
40000 złapanych pakietów. Przy 60000 pakietów prawdopodobieństwo
wynosi około 80%, a przy 85000 około 95%.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -m 755 aircrack-ptw $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/aircrack-ptw
