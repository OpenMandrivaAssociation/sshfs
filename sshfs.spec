Name: sshfs
Version: 3.7.3
Release: 3
Source0: https://github.com/libfuse/sshfs/archive/sshfs-%{version}.tar.gz
Summary: Filesystem based on ssh
URL: https://fuse.sf.net/sshfs.html
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(fuse3)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: meson
BuildRequires: python-docutils

%description
This is a filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy
to set up: i.e. on the server side there's nothing to do.

On the client side mounting the filesystem is as easy as logging into
the server with ssh.

%prep
%setup -qn %{name}-%{name}-%{version}
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
%meson

%build
%meson_build

%install
%meson_install

%files
%{_sbindir}/mount.sshfs
%{_sbindir}/mount.fuse.sshfs
%{_bindir}/sshfs
%{_mandir}/man1/*
