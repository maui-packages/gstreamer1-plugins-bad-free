# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       gstreamer1-plugins-bad-free

# >> macros
# << macros
%define majorminor 1.0

Summary:    GStreamer streaming media framework "bad" plugins
Version:    1.4.1
Release:    1
Group:      Applications/Multimedia
License:    LGPLv2+ and LGPLv2
URL:        http://gstreamer.freedesktop.org/
Source0:    %{name}-%{version}.tar.xz
Source1:    gst-p-bad-cleanup.sh
Source100:  gstreamer1-plugins-bad-free.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.18
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  bzip2-devel
BuildRequires:  check
BuildRequires:  chrpath

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


%package devel
Summary:    GStreamer Base Plugins Development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# Exclude plugins that are not allowed
bash %{SOURCE1}
# << setup

%build
# >> build pre
export CFLAGS="-DG_DISABLE_ASSERT -DG_DISABLE_CAST_CHECKS"
export NOCONFIGURE="1"
%autogen
# << build pre

%configure --disable-static \
    --with-package-name='Maui GStreamer package' \
    --with-package-origin='http://www.maui-project.org/' \
    --enable-experimental \
    --enable-gtk-doc=no \
    --enable-introspection=no \
    --enable-orc \
    --enable-debug \
    --disable-fbdev \
    --disable-decklink \
    --disable-linsys \
    --disable-dts \
    --disable-faac \
    --disable-faad \
    --disable-nas \
    --disable-mimic \
    --disable-libmms \
    --disable-mpeg2enc \
    --disable-mplex \
    --disable-neon \
    --disable-openal \
    --disable-rtmp \
    --disable-xvid \
    --disable-chromaprint \
    --disable-eglgles \
    --disable-flite \
    --disable-mpg123 \
    --disable-ofa \
    --disable-opencv \
    --disable-sbc \
    --disable-spandsp \
    --disable-uvch264 \
    --disable-voamrwbenc \
    --disable-webp \
    --disable-openjpeg

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
%find_lang gst-plugins-bad-%{majorminor}

# Remove files we don't want
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Kill rpath
chrpath --delete %{buildroot}%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
chrpath --delete %{buildroot}%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so

# This is referenced as gstreamer-plugins-bad-free on Mer
cp %{buildroot}%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc %{buildroot}%{_libdir}/pkgconfig/gstreamer-plugins-bad-free-%{majorminor}.pc

# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gst-plugins-bad-%{majorminor}.lang
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING COPYING.LIB README REQUIREMENTS
%{_libdir}/libgst*-%{majorminor}.so.*
%{_libdir}/gstreamer-%{majorminor}/*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/libgst*-%{majorminor}.so
%{_includedir}/gstreamer-%{majorminor}/gst/*
%{_libdir}/pkgconfig/*.pc
# << files devel
