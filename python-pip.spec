%global debug_package %{nil}

Name: python-pip
Epoch: 100
Version: 22.0.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Python package management system
License: MIT
URL: https://github.com/pypa/pip/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pip is a replacement for easy_install. It uses mostly the same
techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python_version_nodots}-pip
Summary: Python package management system
Requires: ca-certificates
Requires: python3
Requires: python3-distutils-extra
Requires: python3-setuptools
Requires: python3-wheel
Provides: python3-pip = %{epoch}:%{version}-%{release}
Provides: python3dist(pip) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pip = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pip) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pip = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pip) = %{epoch}:%{version}-%{release}

%description -n python%{python_version_nodots}-pip
Pip is a replacement for easy_install. It uses mostly the same
techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

%files -n python%{python_version_nodots}-pip
%license LICENSE.txt
%{_bindir}/pip*
%{python3_sitelib}/pip*
%endif

%if 0%{?centos_version} == 800
%package -n platform-python-pip
Summary: Python package management system
Requires: ca-certificates
Requires: python3
Requires: python3-distutils-extra
Requires: python3-setuptools
Requires: python3-wheel
Conflicts: platform-python-pip < %{epoch}:%{version}-%{release}
Conflicts: python3-pip < %{epoch}:%{version}-%{release}

%description -n platform-python-pip
Pip is a replacement for easy_install. It uses mostly the same
techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

%package -n python3-pip
Summary: Python package management system
Requires: platform-python-pip = %{epoch}:%{version}-%{release}
Provides: python3-pip = %{epoch}:%{version}-%{release}
Provides: python3dist(pip) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pip = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pip) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pip = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pip) = %{epoch}:%{version}-%{release}

%description -n python3-pip
Pip is a replacement for easy_install. It uses mostly the same
techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

%files -n platform-python-pip
%license LICENSE.txt
%{_bindir}/pip*
%{python3_sitelib}/pip*

%files -n python3-pip
%license LICENSE.txt
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 800)
%package -n python3-pip
Summary: Python package management system
Requires: ca-certificates
Requires: python3
Requires: python3-distutils-extra
Requires: python3-setuptools
Requires: python3-wheel
Provides: python3-pip = %{epoch}:%{version}-%{release}
Provides: python3dist(pip) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pip = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pip) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pip = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pip) = %{epoch}:%{version}-%{release}

%description -n python3-pip
Pip is a replacement for easy_install. It uses mostly the same
techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

%files -n python3-pip
%license LICENSE.txt
%{_bindir}/pip*
%{python3_sitelib}/pip*
%endif

%changelog
