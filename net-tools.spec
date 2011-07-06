Summary: Basic networking tools
Name: net-tools
Version: 1.60
Release: 102%{?dist}
License: GPL+
Group: System Environment/Base
URL: http://net-tools.berlios.de/
Source0: http://www.tazenda.demon.co.uk/phil/net-tools/net-tools-%{version}.tar.bz2
Source1: net-tools-%{version}-config.h
Source2: net-tools-%{version}-config.make
Source3: ether-wake.c
Source4: ether-wake.8
Source5: mii-diag.c
Source6: mii-diag.8
Source7: iptunnel.8
Source8: ipmaddr.8
Patch1: net-tools-1.57-bug22040.patch
Patch2: net-tools-1.60-miiioctl.patch
Patch3: net-tools-1.60-manydevs.patch
Patch4: net-tools-1.60-virtualname.patch
Patch5: net-tools-1.60-cycle.patch
Patch6: net-tools-1.60-nameif.patch
Patch7: net-tools-1.60-ipx.patch
Patch8: net-tools-1.60-inet6-lookup.patch
Patch9: net-tools-1.60-man.patch
Patch10: net-tools-1.60-gcc33.patch
Patch11: net-tools-1.60-trailingblank.patch
Patch12: net-tools-1.60-interface.patch
Patch14: net-tools-1.60-gcc34.patch
Patch15: net-tools-1.60-overflow.patch
Patch19: net-tools-1.60-siunits.patch
Patch20: net-tools-1.60-trunc.patch
Patch21: net-tools-1.60-return.patch
Patch22: net-tools-1.60-parse.patch
Patch23: net-tools-1.60-netmask.patch
Patch24: net-tools-1.60-ulong.patch
Patch25: net-tools-1.60-bcast.patch
Patch26: net-tools-1.60-mii-tool-obsolete.patch
Patch27: net-tools-1.60-netstat_ulong.patch
Patch28: net-tools-1.60-note.patch
Patch29: net-tools-1.60-num-ports.patch
Patch30: net-tools-1.60-duplicate-tcp.patch
Patch31: net-tools-1.60-statalias.patch
Patch32: net-tools-1.60-isofix.patch
Patch34: net-tools-1.60-ifconfig_ib.patch
Patch35: net-tools-1.60-de.patch
Patch37: net-tools-1.60-pie.patch
Patch38: net-tools-1.60-ifaceopt.patch
Patch39: net-tools-1.60-trim_iface.patch
Patch40: net-tools-1.60-stdo.patch
Patch41: net-tools-1.60-statistics.patch
Patch42: net-tools-1.60-ifconfig.patch
Patch43: net-tools-1.60-arp_overflow.patch
Patch44: net-tools-1.60-hostname_man.patch
Patch45: net-tools-1.60-interface_stack.patch
Patch46: net-tools-1.60-selinux.patch
Patch47: net-tools-1.60-netstat_stop_trim.patch
Patch48: net-tools-1.60-netstat_inode.patch
Patch49: net-tools-1.60-fgets.patch
Patch50: net-tools-1.60-ifconfig_man.patch
Patch51: net-tools-1.60-x25-proc.patch
Patch52: net-tools-1.60-sctp.patch
Patch53: net-tools-1.60-arp_man.patch
Patch54: net-tools-1.60-ifconfig-long-iface-crasher.patch
Patch55: net-tools-1.60-netdevice.patch
Patch56: net-tools-1.60-skip.patch
Patch57: net-tools-1.60-netstat-I-fix.patch
Patch58: net-tools-1.60-nameif_strncpy.patch
Patch59: net-tools-1.60-arp-unaligned-access.patch
Patch60: net-tools-1.60-sctp-quiet.patch
Patch61: net-tools-1.60-remove_node.patch
Patch62: net-tools-1.60-netstat-interfaces-crash.patch
Patch64: net-tools-1.60-ec_hw_null.patch
Patch65: net-tools-1.60-statistics_buffer.patch
Patch66: net-tools-1.60-sctp-addrs.patch
Patch67: net-tools-1.60-i-option.patch
Patch68: net-tools-1.60-a-option.patch
Patch69: net-tools-1.60-clear-flag.patch
Patch70: net-tools-1.60-metric-tunnel-man.patch
Patch71: net-tools-1.60-netstat-probe.patch

# scanf format length fix (non-exploitable)
Patch72: net-tools-1.60-scanf-format.patch

# netstat - avoid name resolution for listening or established sockets (-l) by return fast
Patch73: net-tools-1.60-avoid-name-resolution.patch

# netstat - --continuous should flush stdout
Patch74: net-tools-1.60-continous-flush-stdout.patch

# fix some errors so net-tools can be build with DEBUG defined
Patch75: net-tools-1.60-debug-fix.patch

# let the user know that ifconfig can correctly show only first 8 bytes of Infiniband hw address
Patch76: net-tools-1.60-ib-warning.patch

# notes in man pages, saying that these tools are obsolete
Patch77: net-tools-1.60-man-obsolete.patch

# Bug 322901  Sens negating error in man page translation (arp)
Patch78: net-tools-1.60-man-RHEL-bugs.patch

# handle raw "IP" masqinfo
Patch79: net-tools-1.60-masqinfo-raw-ip.patch

# touch up build system to respect normal toolchain env vars rather than requiring people to set random custom ones
# add missing dependency on version.h to libdir target to fix parallel build failures
# convert -idirafter to -I
Patch80: net-tools-1.60-makefile-berlios.patch

# slattach: use fchown() rather than chown() to avoid race between creation and permission changing
Patch81: net-tools-1.60-slattach-fchown.patch

# Bug 531702: make "hostname -s" display host name cut at the first dot (no matter if the host name resolves or not)
Patch82: net-tools-1.60-hostname-short.patch

# use <linux/mii.h> instead of "mii.h" and fix Bug #491358
Patch83: net-tools-1.60-mii-refactor.patch

# Bug 567272: ifconfig interface:0 del <IP> will remove the Aliased IP on IA64
Patch84: net-tools-1.60-IA64.patch

# interface: fix IPv6 parsing of interfaces with large indexes (> 255)
Patch85: net-tools-1.60-large-indexes.patch

# netstat -s (statistics.c) now uses unsigned long long (instead of int) to handle 64 bit integers (Bug #580054)
Patch86: net-tools-1.60-statistics-doubleword.patch

BuildRequires: gettext, libselinux
BuildRequires: libselinux-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The net-tools package contains basic networking tools,
including ifconfig, netstat, route, and others.
Most of them are obsolete. For replacement check iproute package.

%prep
%setup -q
%patch1 -p1 -b .bug22040
%patch2 -p1 -b .miiioctl
%patch3 -p0 -b .manydevs
%patch4 -p1 -b .virtualname
%patch5 -p1 -b .cycle
%patch6 -p1 -b .nameif
%patch7 -p1 -b .ipx
%patch8 -p1 -b .inet6-lookup
%patch9 -p1 -b .man
%patch10 -p1 -b .gcc33
%patch11 -p1 -b .trailingblank
%patch12 -p1 -b .interface
%patch14 -p1 -b .gcc34
%patch15 -p1 -b .overflow
%patch19 -p1 -b .siunits
%patch20 -p1 -b .trunc
%patch21 -p1 -b .return
%patch22 -p1 -b .parse
%patch23 -p1 -b .netmask
%patch24 -p1 -b .ulong
%patch25 -p1 -b .bcast
%patch26 -p1 -b .obsolete
%patch27 -p1 -b .netstat_ulong
%patch28 -p1 -b .note
%patch29 -p1 -b .num-ports
%patch30 -p1 -b .dup-tcp
%patch31 -p1 -b .statalias
%patch32 -p1 -b .isofix
%patch34 -p1 -b .ifconfig_ib
%patch35 -p1 
%patch37 -p1 -b .pie
%patch38 -p1 -b .ifaceopt
%patch39 -p1 -b .trim-iface
%patch40 -p1 -b .stdo
%patch41 -p1 -b .statistics
%patch42 -p1 -b .iface_drop
%patch43 -p1 -b .overflow
%patch44 -p1 -b .hostname_man
%patch45 -p0 -b .stack
%patch46 -p1 -b .selinux
%patch47 -p1 -b .trim
%patch48 -p1 -b .inode
%patch49 -p1 -b .fgets
%patch50 -p1 -b .inet_addr
%patch51 -p1 -b .x25
%patch52 -p1 -b .sctp
%patch53 -p1
%patch54 -p1 -b .long_iface
%patch55 -p1 -b .netdevice
%patch56 -p1 -b .skip
%patch57 -p1
%patch58 -p1 -b .strncpy
%patch59 -p1 -b .arp-un-access
%patch60 -p1 -b .quiet
%patch61 -p1
%patch62 -p1 -b .iface-crash
%patch64 -p1
%patch65 -p1 -b .buffer
%patch66 -p1 -b .sctp-addrs
%patch67 -p1 -b .i-option
%patch68 -p1 -b .a-option
%patch69 -p1 -b .clear-flag
%patch70 -p1 -b .metric-tunnel-man
%patch71 -p1 -b .probe
%patch72 -p1 -b .scanf-format
%patch73 -p1 -b .avoid-name-resolution
%patch74 -p1 -b .continous-flush-stdout
%patch75 -p1 -b .debug-fix
%patch76 -p1 -b .ib-warning
%patch77 -p1 -b .man-obsolete
%patch78 -p1 -b .man-RHEL-bugs
%patch79 -p1 -b .masqinfo-raw-ip
%patch80 -p1 -b .makefile-berlios
%patch81 -p1 -b .slattach-fchown
%patch82 -p1 -b .hostname-short
%patch83 -p1 -b .mii-refactor
%patch84 -p1 -b .IA64
%patch85 -p1 -b .large-indexes
%patch86 -p1 -b .doubleword

cp %SOURCE1 ./config.h
cp %SOURCE2 ./config.make
cp %SOURCE3 .
cp %SOURCE4 ./man/en_US
cp %SOURCE5 .
cp %SOURCE6 ./man/en_US
cp %SOURCE7 ./man/en_US
cp %SOURCE8 ./man/en_US

%ifarch alpha
perl -pi -e "s|-O2||" Makefile
%endif

#man pages conversion
#french 
iconv -f iso-8859-1 -t utf-8 -o arp.tmp man/fr_FR/arp.8 && mv arp.tmp man/fr_FR/arp.8
iconv -f iso-8859-1 -t utf-8 -o ethers.tmp man/fr_FR/ethers.5 && mv ethers.tmp man/fr_FR/ethers.5
iconv -f iso-8859-1 -t utf-8 -o hostname.tmp man/fr_FR/hostname.1 && mv hostname.tmp man/fr_FR/hostname.1
iconv -f iso-8859-1 -t utf-8 -o ifconfig.tmp man/fr_FR/ifconfig.8 && mv ifconfig.tmp man/fr_FR/ifconfig.8
iconv -f iso-8859-1 -t utf-8 -o netstat.tmp man/fr_FR/netstat.8 && mv netstat.tmp man/fr_FR/netstat.8
iconv -f iso-8859-1 -t utf-8 -o plipconfig.tmp man/fr_FR/plipconfig.8 && mv plipconfig.tmp man/fr_FR/plipconfig.8
iconv -f iso-8859-1 -t utf-8 -o rarp.tmp man/fr_FR/rarp.8 && mv rarp.tmp man/fr_FR/rarp.8
iconv -f iso-8859-1 -t utf-8 -o route.tmp man/fr_FR/route.8 && mv route.tmp man/fr_FR/route.8
iconv -f iso-8859-1 -t utf-8 -o slattach.tmp man/fr_FR/slattach.8 && mv slattach.tmp man/fr_FR/slattach.8
#portugal
iconv -f iso-8859-1 -t utf-8 -o arp.tmp man/pt_BR/arp.8 && mv arp.tmp man/pt_BR/arp.8
iconv -f iso-8859-1 -t utf-8 -o hostname.tmp man/pt_BR/hostname.1 && mv hostname.tmp man/pt_BR/hostname.1
iconv -f iso-8859-1 -t utf-8 -o ifconfig.tmp man/pt_BR/ifconfig.8 && mv ifconfig.tmp man/pt_BR/ifconfig.8
iconv -f iso-8859-1 -t utf-8 -o netstat.tmp man/pt_BR/netstat.8 && mv netstat.tmp man/pt_BR/netstat.8
iconv -f iso-8859-1 -t utf-8 -o rarp.tmp man/pt_BR/rarp.8 && mv rarp.tmp man/pt_BR/rarp.8
iconv -f iso-8859-1 -t utf-8 -o route.tmp man/pt_BR/route.8 && mv route.tmp man/pt_BR/route.8
#german
iconv -f iso-8859-1 -t utf-8 -o arp.tmp man/de_DE/arp.8 && mv arp.tmp man/de_DE/arp.8
iconv -f iso-8859-1 -t utf-8 -o ethers.tmp man/de_DE/ethers.5 && mv ethers.tmp man/de_DE/ethers.5
iconv -f iso-8859-1 -t utf-8 -o hostname.tmp man/de_DE/hostname.1 && mv hostname.tmp man/de_DE/hostname.1
iconv -f iso-8859-1 -t utf-8 -o ifconfig.tmp man/de_DE/ifconfig.8 && mv ifconfig.tmp man/de_DE/ifconfig.8
iconv -f iso-8859-1 -t utf-8 -o netstat.tmp man/de_DE/netstat.8 && mv netstat.tmp man/de_DE/netstat.8
iconv -f iso-8859-1 -t utf-8 -o plipconfig.tmp man/de_DE/plipconfig.8 && mv plipconfig.tmp man/de_DE/plipconfig.8
iconv -f iso-8859-1 -t utf-8 -o rarp.tmp man/de_DE/rarp.8 && mv rarp.tmp man/de_DE/rarp.8
iconv -f iso-8859-1 -t utf-8 -o route.tmp man/de_DE/route.8 && mv route.tmp man/de_DE/route.8
iconv -f iso-8859-1 -t utf-8 -o slattach.tmp man/de_DE/slattach.8 && mv slattach.tmp man/de_DE/slattach.8

%build
export CFLAGS="$RPM_OPT_FLAGS $CFLAGS"

make
gcc $RPM_OPT_FLAGS -o ether-wake ether-wake.c
gcc $RPM_OPT_FLAGS -o mii-diag mii-diag.c

%install
rm -rf %{buildroot}
mv man/de_DE man/de
mv man/fr_FR man/fr
mv man/pt_BR man/pt

make BASEDIR=%{buildroot} mandir=%{_mandir} install

install -m 755 ether-wake %{buildroot}/sbin
install -m 755 mii-diag %{buildroot}/sbin

rm %{buildroot}/sbin/rarp
rm %{buildroot}%{_mandir}/man8/rarp.8*
rm %{buildroot}%{_mandir}/de/man8/rarp.8*
rm %{buildroot}%{_mandir}/fr/man8/rarp.8*
rm %{buildroot}%{_mandir}/pt/man8/rarp.8*

mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ethers
echo "# see man ethers for syntax" > %{buildroot}%{_sysconfdir}/ethers

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
/bin/*
/sbin/*
%{_mandir}/man[158]/*
%lang(de)	%{_mandir}/de/man[158]/*
%lang(fr)	%{_mandir}/fr/man[158]/*
%lang(pt)	%{_mandir}/pt/man[158]/*
%config(noreplace) %{_sysconfdir}/ethers

%changelog
* Wed Apr  7 2010  Jiri Popelka <jpopelka@redhat.com> - 1.60-102
- fixed statistics.c to use unsigned long long (instead of int) to handle 64 bit integers (Bug #580054)
- fixed typo in statistics.c
- interface slip: cast keepalive/outfill to unsigned long to fix warnings on 64bit hosts
- interface: fix IPv6 parsing of interfaces with large indexes (> 255)

* Mon Feb 22 2010  Jiri Popelka <jpopelka@redhat.com> - 1.60-101
- ifconfig interface:0 del <IP> will remove the Aliased IP on IA64 (#567272)

* Tue Jan 12 2010  Jiri Popelka <jpopelka@redhat.com> - 1.60-100
- fixed overflow patch (#554695)

* Thu Dec  3 2009  Jiri Popelka <jpopelka@redhat.com> - 1.60-99
- return defining of BuildRoot even it's no longer necessary
  (https://fedoraproject.org/wiki/Packaging:Guidelines#BuildRoot_tag)
  to silent rpmlint false warning

* Wed Nov  4 2009  Jiri Popelka <jpopelka@redhat.com> - 1.60-98
- in mii-tool.c use <linux/mii.h> instead of "mii.h" and fix Bug #491358

* Thu Oct 29 2009  Jiri Popelka <jpopelka@redhat.com> - 1.60-97
- Make "hostname -s" display host name cut at the first dot (no
  matter if the host name resolves or not) (bug #531702)

* Tue Sep 30 2009  Jiri Popelka <jpopelka@redhat.com> - 1.60-96
- netplug moved to separate package
- #319981 and #322901 - minor man pages changes
- applied changes from berlios cvs, which fix: Berlios #16232, Gentoo #283759 and polish Makefile and slattach 

* Tue Sep 1 2009  Jiri Popelka <jpopelka@redhat.com> - 1.60-95
- netstat - avoid name resolution for listening or established sockets (-l) by return fast. 
- netstat - --continuous should flush stdout
- added missing man pages (iptunnel, ipmaddr, netplug, netplug.d, netplugd.conf)
- added note about obsolete commands to existing man pages 
- let the user know that ifconfig can correctly show only first 8 bytes of Infiniband hw address

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009  Jiri Popelka <jpopelka@redhat.com> - 1.60-93
- scanf format length fix (non exploitable?) from Fabian Hugelshofer <hugelshofer2006@gmx.ch>
- URL tag changed to http://net-tools.berlios.de/

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 16 2008 Zdenek Prikryl <zprikryl@redhat.com> - 1.60-91
- fixed tcp timers info in netstat (#466845)

* Thu Sep 25 2008 Zdenek Prikryl <zprikryl@redhat.com> - 1.60-90
- fixed ifconfig's man page (#454271, #432328)

* Tue Jul 15 2008 Zdenek Prikryl <zprikryl@redhat.com> - 1.60-89
- fixed man pages for arp (#446195)
- fixed netstat --interfaces option (#446187)
- fixed clearing flags in ifconfig (#450252)

* Tue Jul  8 2008 Radek Vokál <rvokal@redhat.com> - 1.60-88
- netstat displays correct sctp statistics (#445535) <zprikryl@redhat.com>

* Tue Mar  4 2008 Radek Vokál <rvokal@redhat.com> - 1.60-87
- fix buffer for newer kernels (#435554)

* Mon Feb 25 2008 Radek Vokal <rvokal@redhat.com> - 1.60-86
- fix for GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.60-85
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Radek Vokál <rvokal@redhat.com> - 1.60-84
- rebuilt

* Fri Jun  8 2007 Radek Vokál <rvokal@redhat.com> - 1.60-83
- fix netplugd init script (#242919)

* Tue May 22 2007 Radek Vokál <rvokal@redhat.com> - 1.60-82
- better SELinux patch by <dwalsh@redhat.com>

* Tue Mar 27 2007 Radek Vokál <rvokal@redhat.com> - 1.60-81
- fix segfault for empty interface (#234045)

* Thu Mar 15 2007 Radek Vokál <rvokal@redhat.com> - 1.60-80
- we don't have -n/--node option (#225554)

* Thu Feb 22 2007 Radek Vokál <rvokal@redhat.com> - 1.60-79
- quiet sctp (#229232)

* Mon Feb 19 2007 Radek Vokál <rvokal@redhat.com> - 1.60-78
- spec file cleanup (#226193)

* Tue Jan 30 2007 Radek Vokál <rvokal@redhat.com> - 1.60-77
- touch /etc/ethers (#225381)

* Wed Dec 27 2006 Radek Vokál <rvokal@redhat.com> - 1.60-76
- fix arp unaligned access (#220438)

* Wed Oct  4 2006 Radek Vokal <rvokal@redhat.com> - 1.60-75
- fix nameif crash for 16char long interface names (#209120)

* Mon Oct  2 2006 Radek Vokal <rvokal@redhat.com> - 1.60-74
- fix -I option for nestat, works as -I=eth0 again.
- add dist tag

* Mon Aug  7 2006 Radek Vokal <rvokal@redhat.com> - 1.60-73
- directory entries . and .. should be skipped

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.60-72.1
- rebuild

* Wed Jun  7 2006 Radek Vokal <rvokal@redhat.com> - 1.60-72
- switch --trim to --notrim .. make it less confusing 

* Fri May 19 2006 Radek Vokal <rvokal@redhat.com> - 1.60-71
- BuildRequires: libselinux-devel (#191737)

* Tue May 09 2006 Radek Vokál <rvokal@redhat.com> - 1.60-70
- add netdevice.h, fix x25
- fix ifconfig crash when interface name is too long (#190703)

* Tue May 02 2006 Radek Vokál <rvokal@redhat.com> - 1.60-69
- fix arp man page to correspond to man ethers (#190425)

* Fri Apr 14 2006 Radek Vokál <rvokal@redhat.com> - 1.60-68
- display sctp connections using netstat -S <jbj@redhat.com>

* Thu Apr 13 2006 Radek Vokál <rvokal@redhat.com> - 1.60-67
- fix wrong definition of _PATH_PROCNET_X25_ROUTE (#188786)

* Thu Apr 06 2006 Radek Vokál <rvokal@redhat.com> - 1.60-66
- add note about -T to netstat

* Thu Mar 30 2006 Radek Vokál <rvokal@redhat.com> - 1.60-65
- add note to ifconfig(8) about supported format for IPv4 addresses (#176661)

* Thu Mar 16 2006 Radek Vokál <rvokal@redhat.com> - 1.60-64
- remove duplicate arp entries (#185604)

* Thu Feb 23 2006 Radek Vokál <rvokal@redhat.com> - 1.60-63
- show inodes in netstat (#180974)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.60-62.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Radek Vokál <rvokal@redhat.com> - 1.60-62
- new option for netstat - -T stops trimming remote and local addresses (#176465)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.60-61.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb 06 2006 Radek Vokál <rvokal@redhat.com> 1.60-61
- mii-tool manpage fixed (#180055)

* Tue Jan 17 2006 Radek Vokal <rvokal@redhat.com> 1.60-60
- forget to enable the new selinux option :( - config.make changed

* Tue Jan 17 2006 Radek Vokal <rvokal@redhat.com> 1.60-59
- new option for nestat, -Z shows selinux context. Patch by <dwalsh@redhat.com>

* Mon Jan 02 2006 Radek Vokal <rvokal@redhat.com> 1.60-58
- clear static buffers in interface.c by <drepper@redhat.com> (#176714)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 15 2005 Radek Vokal <rvokal@redhat.com> 1.60-57
- add note to hostname man page about gethostbyname() (#166581)
- don't ship any rarp man page (#170537)

* Wed Aug 03 2005 Radek Vokal <rvokal@redhat.com> 1.60-56
- fixed buffer overflow in arp (#164695)

* Wed Jul 20 2005 Radek Vokal <rvokal@redhat.com> 1.60-55
- ifconfig - fixed virtual interface dropping (#162888)

* Wed Jun 22 2005 Radek Vokal <rvokal@redhat.com> 1.60-54
- fr man pages are back (#159702)

* Mon Jun 06 2005 Radek Vokal <rvokal@redhat.com> 1.60-53
- etherwake man page changed to ether-wake (#159156)

* Tue Apr 26 2005 Radek Vokal <rvokal@redhat.com> 1.60-52
- don't show "duplicate line" warning (#143933)
- netstat has new statistcs (#133032)
- /etc/neplug is owned by net-tools (#130621)

* Tue Apr 05 2005 Radek Vokal <rvokal@redhat.com> 1.60-51
- flush output in mii-tool (#152568)

* Wed Mar 30 2005 Radek Vokal <rvokal@redhat.com> 1.60-50
- added mii-diag tool
- added newer ether-wake
- remove useless -i option from ifconfig
- stop trimming interface names (#152457)

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 01 2005 Radek Vokal <rvokal@redhat.com> 1.60-48
- behaviour of netstat -i option changed (#115987)
- netstat -i shows all interface, -I<Iface> only one

* Mon Feb 28 2005 Radek Vokal <rvokal@redhat.com> 1.60-47
- added RPM_OPT_FLAGS
- execshield patch for netplug <t8m@redhat.com>

* Wed Feb 16 2005 Radek Vokal <rvokal@redhat.com> 1.60-46
- small typo in german translation (#148775)

* Wed Feb 09 2005 Radek Vokal <rvokal@redhat.com> 1.60-45
- included infiniband support (#147396) <tduffy@sun.com>
- added etherwake man page

* Mon Feb 07 2005 Radek Vokal <rvokal@redhat.com> 1.60-44
- net-plug-1.2.9 - no changes, upstream included Red Hat patches
- ether-wake-1.08 - few changes in implementation (#145718)

* Mon Jan 10 2005 Radek Vokal <rvokal@redhat.com> 1.60-43
- don't report statistics for virtual devices (#143981) <kzak@redhat.com>
- fixing translation headers - content type format
- kill bitkeeper warning messages

* Fri Dec 03 2004 Radek Vokal <rvokal@redhat.com> 1.60-42
- filter out duplicate tcp entries (#139407)

* Thu Nov 25 2004 Radek Vokal <rvokal@redhat.com> 1.60-41
- added note to hostname(1) (#140239)
- fixed --num-ports option for netstat (#115100)

* Thu Nov 11 2004 Radek Vokal <rvokal@redhat.com> 1.60-40
- mii-tool(8) fixed, labeled as obsolete, added info (#138687)
- netstat crashing on i64 fixed (#138804) Patch by <Andreas.Hirstius@cern.ch>

* Thu Nov 04 2004 Radek Vokal <rvokal@redhat.com> 1.60-39
- IBM patch for netstat -s returning negative values on 64bit arch (#144064)
- broadcast calulated if only netmask provided (#60509)

* Tue Nov 02 2004 Radek Vokal <rvokal@redhat.com> 1.60-38
- fixed fail to assign the specified netmask before adress is assigned
- patch by Malita, Florin <florin.malita@glenayre.com>

* Wed Sep 29 2004 Radek Vokal <rvokal@redhat.com> 1.60-37
- spec file updated, added conversion for french and portugal man pages to UTF-8

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 1.60-36
- parse error fixed (#131539)

* Fri Sep 03 2004 Radek Vokal <rvokal@redhat.com> 1.60-35
- The return value of nameif was wrong (#129032) - patch from Fujitsu QA 

* Tue Aug 30 2004 Radek Vokal <rvokal@redhat.com> 1.60-34
- Trunc patch added (#128359)

* Mon Aug 30 2004 Radek Vokal <rvokal@redhat.com> 1.60-33
- Added patch for SI units by Tom "spot" Callaway <tcallawa@redhat.com> #118006

* Tue Aug 17 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-32
- Fix installopts for netplug.

* Sun Aug 08 2004 Alan Cox <alan@redhat.com> 1.60-31
- Build requires gettext.

* Mon Aug 02 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-30
- Update to latest netplugd version.

* Mon Jul 12 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-29
- Fixed initscript patch for netplug (#127351)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 14 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-27
- Fixed compiler warning/error in netplug.
- Updated to netplug-1.2.6 for security update and fixes.

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-26
- Updated netplugd to latest upstream version.
- Fixed execshield problem in main.c of netplugd.

* Thu Apr 15 2004 Phil Knirsch <pknirsch@redhat.com> 1.60-25
- Fixed several possible buffer overflows (#120343)

* Tue Mar 30 2004 Harald Hoyer <harald@redhat.com> - 1.60-24
- fixed compilation with gcc34

* Tue Mar 23 2004 Karsten Hopp <karsten@redhat.de> 1.60-23 
- add chkconfig call in post and preun, fix init script (#116555)

* Thu Feb 19 2004 Phil Knirsch <pknirsch@redhat.com>
- Added netplug-1.2.1 to net-tools (FR #103419).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Aug 25 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-20.1
-rebuilt

* Mon Aug 25 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-20
- interface option now works as described in the man page (#61113).

* Tue Aug 19 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-19.1
- rebuilt

* Tue Aug 19 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-19
- Fixed trailing blank bug in hostname output (#101263).
- Remove -O2 fir alpha (#78955).
- Updated netstat statistic output, was still broken.

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-18.1
- rebuilt

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-18
- fix ether-wake.c build with gcc 3.3
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-16.1
- Bumped release and rebuilt

* Fri May 23 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-16
- Fixed ether-wake usage output (#55801).

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.60-15
- fix build with gcc 3.3

* Thu May 22 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-14
- Fixed wrong manpage (#55473).

* Wed May 21 2003 Phil Knirsch <pknirsch@redhat.com>
- Added inet6-lookup patch from John van Krieken (#84108).
- Fixed outdated link in ifconfig manpage (#91287).

* Tue May 20 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed incorrect address display for ipx (#46434).
- Fixed wrongly installed manpage dirs (#50664).

* Wed Mar 19 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-13
- Fixed nameif problem (#85748).

* Fri Feb 07 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-12
- Fixed -s parameter.
- Fix /proc statistics for -nic operation.
- Fixed -i operation in general.

* Mon Jan 27 2003 Phil Knirsch <pknirsch@redhat.com> 1.60-11
- Disable smp build.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.60-10
- rebuilt

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 1.60-9
- Rebuild
- Copyright -> License.

* Thu Dec 05 2002 Elliot Lee <sopwith@redhat.com> 1.60-8
- Rebuild

* Tue Aug 06 2002 Phil Knirsch <pknirsch@redhat.com> 
- Added patch from Norm for a corrected output.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 12 2002 Jeremy Katz <katzj@redhat.com>
- fix nstrcmp() to be correct in the case where there are many devices 
  of the same type, eg, "eth10" > "eth1"  (#61436)

* Tue Jul 31 2001 Bill Nottingham <notting@redhat.com>
- do *not* use SIOCDEVPRIVATE for MII ioctls

* Fri Jun  1 2001 Preston Brown <pbrown@redhat.com>
- include wake-on-lan wakeup utility, ether-wake by Donald Becker

* Wed Apr 18 2001 Crutcher Dunnavant <crutcher@redhat.com>
- itterate to 1.60

* Sun Apr  8 2001 Preston Brown <pbrown@redhat.com>
- use find_lang macro
- less specific locale dirs for man pages

* Mon Apr  2 2001 Preston Brown <pbrown@redhat.com>
- don't use this version of rarp, doesn't work with our 2.4.

* Tue Feb  6 2001 Crutcher Dunnavant <crutcher@redhat.com>
- fixed man page typo, closing bug #25921

* Fri Feb  1 2001 Crutcher Dunnavant <crutcher@redhat.com>
- applied twaugh's patch to close bug #25474
- which was a buffer length bug.

* Wed Dec 27 2000 Jeff Johnson <jbj@redhat.com>
- locales not initialized correctly (#20570).
- arp: document -e option (#22040).

* Sat Oct  7 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.57.
- MTU (and other) option(s) not parsed correctly (#9215).
- allow more granularity iwth --numeric (#9129).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.56.
- FHS packaging.

* Sat Apr 15 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.55.

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Fri Jan 14 2000 Jeff Johnson <jbj@redhat.com>
- fix "netstat -ci" (#6904).
- document more netstat options (#7429).

* Thu Jan 13 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.54.
- enable "everything but DECnet" including IPv6.

* Sun Aug 29 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.53.

* Wed Jul 28 1999 Jeff Johnson <jbj@redhat.com>
- plug "netstat -c" fd leak (#3620).

* Thu Jun 17 1999 Jeff Johnson <jbj@redhat.com>
- plug potential buffer overruns.

* Sat Jun 12 1999 John Hardin <jhardin@wolfenet.com>
- patch to recognize ESP and GRE protocols for VPN masquerade

* Fri Apr 23 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.52.

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- update interface statistics continuously (#1323)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.51.
- strip binaries.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.50.
- added slattach/plipconfig/ipmaddr/iptunnel commands.
- enabled translated man pages.

* Tue Dec 15 1998 Jakub Jelinek <jj@ultra.linux.cz>
- update to 1.49.

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.48.

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.47.

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.46

* Thu Jul  9 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include ethers.5

* Thu Jun 11 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 1.45
- patched hostname.c to initialize buffer
- patched ax25.c to use kernel headers

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- added config patch

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- changed to net-tools 1.432
- removed old glibc 2.1 patch
 
* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added extra patches for glibc 2.1

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- included complete set of network protocols (some were removed for
  initial glibc work)

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- updated glibc patch for glibc 2.0.5

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- updated to 1.33
