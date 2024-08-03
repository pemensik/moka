# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate moka

Name:           rust-moka
Version:        0.12.8
Release:        %autorelease
Summary:        Fast and concurrent cache library inspired by Java Caffeine

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/moka
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          moka-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
Patch:          moka-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A fast and concurrent cache library inspired by Java Caffeine.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/MIGRATION-GUIDE.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-lock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-lock-devel %{_description}

This package contains library source intended for building other packages which
use the "async-lock" feature of the "%{crate}" crate.

%files       -n %{name}+async-lock-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+atomic64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atomic64-devel %{_description}

This package contains library source intended for building other packages which
use the "atomic64" feature of the "%{crate}" crate.

%files       -n %{name}+atomic64-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+event-listener-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+event-listener-devel %{_description}

This package contains library source intended for building other packages which
use the "event-listener" feature of the "%{crate}" crate.

%files       -n %{name}+event-listener-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+future-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+future-devel %{_description}

This package contains library source intended for building other packages which
use the "future" feature of the "%{crate}" crate.

%files       -n %{name}+future-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-util-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%files       -n %{name}+futures-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+quanta-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quanta-devel %{_description}

This package contains library source intended for building other packages which
use the "quanta" feature of the "%{crate}" crate.

%files       -n %{name}+quanta-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sync-devel %{_description}

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%files       -n %{name}+sync-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-debug-counters-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-debug-counters-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable-debug-counters" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-debug-counters-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f future,sync

%build
%cargo_build -f future,sync

%install
%cargo_install -f future,sync

%if %{with check}
%check
%cargo_test -f future,sync
%endif

%changelog
%autochangelog