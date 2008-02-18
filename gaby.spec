Summary:	Small personal databases manager for Linux
Name:		gaby
Version:	2.0.3
Release:	%mkrel 8
License:	GPL
Group:		Databases

Source:		http://www.0d.be/projects/%{name}/archives/%{name}-%{version}.tar.bz2
Patch0:		gaby-2.0.2-gcc-build-fix-patch

Url:		http://www.0d.be/projects/%{name}
BuildRoot:	%_tmppath/%name-%version-root

BuildRequires:	libesound-devel python-gtk-devel libglade2.0-devel libORBit2-devel
BuildRequires:	docbook-utils docbook-dtd30-sgml
BuildRequires:	libglib-devel chrpath gtk+1.2-devel python-devel
BuildConflicts: %{_lib}gdk-pixbuf2-devel libglade0-devel libgnome32-devel

%description
Gaby is a small personal databases manager for Linux using GTK+ and Gnome 
(if available) for its GUI.

It was designed to provide straight-forward access to databases a 'normal' 
user would like (addresses, books, ...) (see the descfiles page) while 
keeping the ability to easily create databases for other needs. On a 
technical side it was designed with extensibility in mind and thus use 
relies a lot on plug-ins; and an extension language not unlike The Gimp 
script-fus is available (an embedded Python). 

%prep
%setup -q
%patch0 -p1
%if %_lib == lib64
  sed -i 's|lib/python|lib64/python|g' configure
  sed -i 's|lib/libpython|lib64/libpython|g' configure
%endif

%build
export CFLAGS="$RPM_OPT_FLAGS -L%{_libdir}"
%configure --disable-gnome --disable-rpath
%make

%install
rm -fr %buildroot
%makeinstall

find $RPM_BUILD_ROOT -name '*.a' | xargs rm -fr
find $RPM_BUILD_ROOT -name '*.so' | xargs chrpath -d
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*

# (sb) menu item

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Gaby
Comment=Personal Database Manager
Exec=%{_bindir}/%{name}
Icon=databases_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Databases;Database;
EOF

# (sb) remove these symlinks that conflict with other packages
rm -f $RPM_BUILD_ROOT%{_bindir}/{gnomecard,videobase,gcd,appindex}
mv $RPM_BUILD_ROOT%{_bindir}/gbc $RPM_BUILD_ROOT%{_bindir}/gbc-gaby

%post
%update_menus

%postun
%clean_menus

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/desc.*
%{_bindir}/gaby*
%{_bindir}/gbc-gaby
%{_bindir}/app*
%{_bindir}/gcd*
%{_bindir}/gnome*
%{_bindir}/video*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plug-ins
%dir %{_libdir}/%{name}/plug-ins/actions
%{_libdir}/%{name}/plug-ins/actions/libcd.la
%{_libdir}/%{name}/plug-ins/actions/libcd.so
%{_libdir}/%{name}/plug-ins/actions/libnet.la
%{_libdir}/%{name}/plug-ins/actions/libnet.so
%{_libdir}/%{name}/plug-ins/actions/libstat.la
%{_libdir}/%{name}/plug-ins/actions/libstat.so
%dir %{_libdir}/%{name}/plug-ins/formats
%{_libdir}/%{name}/plug-ins/formats/infos
%{_libdir}/%{name}/plug-ins/formats/libaddressbook.la
%{_libdir}/%{name}/plug-ins/formats/libaddressbook.so
%{_libdir}/%{name}/plug-ins/formats/libappindex.la
%{_libdir}/%{name}/plug-ins/formats/libappindex.so
%{_libdir}/%{name}/plug-ins/formats/libcsv.la
%{_libdir}/%{name}/plug-ins/formats/libcsv.so
%{_libdir}/%{name}/plug-ins/formats/libdbase.la
%{_libdir}/%{name}/plug-ins/formats/libdbase.so
%{_libdir}/%{name}/plug-ins/formats/libdpkg.la
%{_libdir}/%{name}/plug-ins/formats/libdpkg.so
%{_libdir}/%{name}/plug-ins/formats/libgaby.la
%{_libdir}/%{name}/plug-ins/formats/libgaby.so
%{_libdir}/%{name}/plug-ins/formats/libgaby1.la
%{_libdir}/%{name}/plug-ins/formats/libgaby1.so
%{_libdir}/%{name}/plug-ins/formats/libnosql.la
%{_libdir}/%{name}/plug-ins/formats/libnosql.so
%{_libdir}/%{name}/plug-ins/formats/libpilot.la
%{_libdir}/%{name}/plug-ins/formats/libpilot.so
%{_libdir}/%{name}/plug-ins/formats/libvcard.la
%{_libdir}/%{name}/plug-ins/formats/libvcard.so
%{_libdir}/%{name}/plug-ins/formats/libvideobase.la
%{_libdir}/%{name}/plug-ins/formats/libvideobase.so
%dir %{_libdir}/%{name}/plug-ins/interpreter
%{_libdir}/%{name}/plug-ins/interpreter/libpython.la
%{_libdir}/%{name}/plug-ins/interpreter/libpython.so
%dir %{_libdir}/%{name}/plug-ins/print
%{_libdir}/%{name}/plug-ins/print/html.dsc
%{_libdir}/%{name}/plug-ins/print/html.py
%{_libdir}/%{name}/plug-ins/print/html.xml
%{_libdir}/%{name}/plug-ins/print/infos
%{_libdir}/%{name}/plug-ins/print/latex.dsc
%{_libdir}/%{name}/plug-ins/print/latex.py
%{_libdir}/%{name}/plug-ins/print/latex.xml
%{_libdir}/%{name}/plug-ins/print/lout.dsc
%{_libdir}/%{name}/plug-ins/print/lout.py
%{_libdir}/%{name}/plug-ins/print/lout.xml
%{_libdir}/%{name}/plug-ins/print/merging.dsc
%{_libdir}/%{name}/plug-ins/print/merging.py
%{_libdir}/%{name}/plug-ins/print/merging.xml
%dir %{_libdir}/%{name}/plug-ins/view
%{_libdir}/%{name}/plug-ins/view/libfilter.la
%{_libdir}/%{name}/plug-ins/view/libfilter.so
%{_libdir}/%{name}/plug-ins/view/libform.la
%{_libdir}/%{name}/plug-ins/view/libform.so
%{_libdir}/%{name}/plug-ins/view/libgenealogy.la
%{_libdir}/%{name}/plug-ins/view/libgenealogy.so
%{_libdir}/%{name}/plug-ins/view/libhello.la
%{_libdir}/%{name}/plug-ins/view/libhello.so
%{_libdir}/%{name}/plug-ins/view/liblist.la
%{_libdir}/%{name}/plug-ins/view/liblist.so
%{_libdir}/%{name}/plug-ins/view/libminiform.la
%{_libdir}/%{name}/plug-ins/view/libminiform.so
%{_libdir}/%{name}/plug-ins/view/libsearch.la
%{_libdir}/%{name}/plug-ins/view/libsearch.so
%{_libdir}/%{name}/plug-ins/view/libxlist.la
%{_libdir}/%{name}/plug-ins/view/libxlist.so
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/gaby_tips.txt
%lang(de) %{_datadir}/%{name}/gaby_tips_de.txt
%lang(fi) %{_datadir}/%{name}/gaby_tips_fi.txt
%lang(fr) %{_datadir}/%{name}/gaby_tips_fr.txt
%lang(no) %{_datadir}/%{name}/gaby_tips_no.txt
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/gabyform.glade
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/scripts/actions
%{_datadir}/%{name}/scripts/actions/example
%{_datadir}/%{name}/scripts/actions/hello.py
%{_datadir}/%{name}/scripts/actions/nb_records.py
%{_datadir}/%{name}/scripts/actions/set_default_country.py
%{_datadir}/%{name}/scripts/actions/show_phonebook.py
%{_datadir}/%{name}/scripts/actions/tips.py
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/gaby.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/gaby.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gaby.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/gaby.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/gaby.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/gaby.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/gaby.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/gaby.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/gaby.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/gaby.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/gaby.mo
%{_mandir}/man1/gaby.*
%{_mandir}/man1/gabybuilder.*
%{_datadir}/applications/%{name}.desktop


