%define major 0
%define snapshot 20170221

Summary:        QtQuick and Wayland based shell for convergence
Name:           liri-shell
Version:        0.9.0

%if "%{snapshot}" != ""
# snapshot here
%define tarname %{name}-%{version}-%{snapshot}
Release:        1.%{snapshot}.1
Source0:        %{name}-%{version}-%{snapshot}.tar.xz
%else
# official release here
Release:        1
Source0:	https://github.com/lirios/shell/releases/download/v%{version}/%{name}-%{version}.tar.xz
%define tarname %{name}-%{version}
%endif

License:        LGPLv3
Url:            https://github.com/lirios

BuildRequires:  cmake
BuildRequires:	cmake(Vibe)
BuildRequires:	cmake(Fluid)
BuildRequires:	pam-devel
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	cmake(QtAccountsService)
BuildRequires:	cmake(LiriWayland)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5QuickTest)

%description
QtQuick and Wayland based shell for convergence

%prep
%setup -qn %{tarname}
%apply_patches

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/liri-session
%{_bindir}/%{name}
%{_userunitdir}/liri.service
%{_userunitdir}/liri.target
%{_libdir}/libexec/liri-shell-helper
%{_libdir}/qml/Liri/Launcher/liblauncherplugin.so
%{_libdir}/qml/Liri/Launcher/plugins.qmltypes
%{_libdir}/qml/Liri/Launcher/qmldir
%{_libdir}/qml/Liri/LoginManager/libloginmanagerplugin.so
%{_libdir}/qml/Liri/LoginManager/plugins.qmltypes
%{_libdir}/qml/Liri/LoginManager/qmldir
%{_libdir}/qml/Liri/Shell/Background.qml
%{_libdir}/qml/Liri/Shell/DateTime.qml
%{_libdir}/qml/Liri/Shell/DateTimeIndicator.qml
%{_libdir}/qml/Liri/Shell/Indicator.qml
%{_libdir}/qml/Liri/Shell/LoginGreeter.qml
%{_libdir}/qml/Liri/Shell/PanelItem.qml
%{_libdir}/qml/Liri/Shell/UserDelegate.qml
%{_libdir}/qml/Liri/Shell/libshellplugin.so
%{_libdir}/qml/Liri/Shell/plugins.qmltypes
%{_libdir}/qml/Liri/Shell/qmldir
%{_datadir}/wayland-sessions/liri.desktop
