# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global bundle org.osgi.foundation
%global felixdir %{_javadir}/felix
%global POM %{_mavenpomdir}/JPP.felix-%{bundle}.pom

Name:    felix-osgi-foundation
Version: 1.2.0
Release: 6
Summary: Felix OSGi Foundation EE Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

Patch0: felix-osgi-foudantion-pom-target.patch

BuildArch: noarch

BuildRequires: java-devel >= 0:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit4

Requires: java >= 0:1.6.0

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1 -b build_target

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%__mkdir_p $MAVEN_REPO_LOCAL

mvn-jpp -e \
  -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
  install javadoc:javadoc

%install
# jar
install -pD -T -m 644 target/%{bundle}-%{version}.jar \
  %{buildroot}%{felixdir}/%{bundle}.jar

# pom
install -pD -T -m 644 pom.xml %{buildroot}%{POM}
%add_to_maven_depmap org.apache.felix %{bundle} %{version} JPP/felix %{bundle}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%pre javadoc
# workaround for rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%defattr(-,root,root,-)
%doc LICENSE
%{felixdir}
%{POM}
%config(noreplace) %{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

