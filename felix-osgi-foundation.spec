%{?_javapackages_macros:%_javapackages_macros}
%global bundle org.osgi.foundation

Name:    felix-osgi-foundation
Version: 1.2.0
Release: 14.2
Summary: Felix OSGi Foundation EE Bundle

License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4
BuildRequires: mockito
BuildRequires: mvn(org.apache.felix:felix:pom:)
Requires: java >= 1:1.6.0

%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc

Summary:        API documentation for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 05 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-14
- Update for latest guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-12
- Add missing BR: maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-10
- Install LICENSE and NOTICE
- Fix directory permissions
- Remove rpm bug workaround

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-7
- Build with maven 3.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-5
- Update maven plug-in BRs.

* Mon Dec 13 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-4
- Versionless jars & javadocs
- Fix pom filename (#655800)

* Wed Jun 30 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.0-3
- The javadoc subpackage should have requires on jpackage-utils
- Use the mavenpomdir macro
- Rename the mavenPOM macro to publicPOM

* Tue Jun 29 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.0-2
- Use maven to build the project instead of ant

* Thu Jun 24 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.0-1
- Release 1.2.0
