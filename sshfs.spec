Name: sshfs
Version: 2.7
Release: 1.1
Source0: https://github.com/libfuse/sshfs/releases/download/sshfs-2.7/%{name}-%{version}.tar.gz
Summary: Filesystem based on ssh
URL: http://fuse.sf.net/sshfs.html
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gthread-2.0)

%description
This is a filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy
to set up: i.e. on the server side there's nothing to do.

On the client side mounting the filesystem is as easy as logging into
the server with ssh.

%prep
%setup -q
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/sshfs
%{_mandir}/man1/*
