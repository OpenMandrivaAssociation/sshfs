Name: sshfs
Version: 2.5
Release: 5
Source0: http://cznic.dl.sourceforge.net/project/fuse/sshfs-fuse/%{version}/sshfs-fuse-%{version}.tar.gz
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
%setup -q -n %{name}-fuse-%{version}
export CFLAGS="%{optflags} -fuse-ld=bfd"
export LDFLAGS="%{optflags} -fuse-ld=bfd"
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/sshfs
%{_mandir}/man1/*
