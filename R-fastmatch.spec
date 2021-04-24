#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fastmatch
Version  : 1.1.0
Release  : 30
URL      : https://cran.r-project.org/src/contrib/fastmatch_1.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fastmatch_1.1-0.tar.gz
Summary  : Fast match() function
Group    : Development/Tools
License  : GPL-2.0
Requires: R-fastmatch-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
that require repeated look-ups. It is slightly faster that R's
	built-in match() function on first match against a table, but
	extremely fast on any subsequent lookup as it keeps the hash
	table in memory.

%package lib
Summary: lib components for the R-fastmatch package.
Group: Libraries

%description lib
lib components for the R-fastmatch package.


%prep
%setup -q -c -n fastmatch
cd %{_builddir}/fastmatch

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589510906

%install
export SOURCE_DATE_EPOCH=1589510906
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastmatch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastmatch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastmatch
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fastmatch || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fastmatch/DESCRIPTION
/usr/lib64/R/library/fastmatch/INDEX
/usr/lib64/R/library/fastmatch/Meta/Rd.rds
/usr/lib64/R/library/fastmatch/Meta/features.rds
/usr/lib64/R/library/fastmatch/Meta/hsearch.rds
/usr/lib64/R/library/fastmatch/Meta/links.rds
/usr/lib64/R/library/fastmatch/Meta/nsInfo.rds
/usr/lib64/R/library/fastmatch/Meta/package.rds
/usr/lib64/R/library/fastmatch/NAMESPACE
/usr/lib64/R/library/fastmatch/NEWS
/usr/lib64/R/library/fastmatch/R/fastmatch
/usr/lib64/R/library/fastmatch/R/fastmatch.rdb
/usr/lib64/R/library/fastmatch/R/fastmatch.rdx
/usr/lib64/R/library/fastmatch/help/AnIndex
/usr/lib64/R/library/fastmatch/help/aliases.rds
/usr/lib64/R/library/fastmatch/help/fastmatch.rdb
/usr/lib64/R/library/fastmatch/help/fastmatch.rdx
/usr/lib64/R/library/fastmatch/help/paths.rds
/usr/lib64/R/library/fastmatch/html/00Index.html
/usr/lib64/R/library/fastmatch/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fastmatch/libs/fastmatch.so
/usr/lib64/R/library/fastmatch/libs/fastmatch.so.avx2
