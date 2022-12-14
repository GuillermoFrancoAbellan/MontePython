#Makefile --- WMAP Likelihood code...

CFITSIO=/usr/local

#
#			Non-test object files.
#
WMAPLIB = libwmap9.a
OBJS = read_archive_map.o \
	read_fits.o \
	healpix_types.o \
	br_mod_dist.o \
	WMAP_9yr_options.o \
	WMAP_9yr_util.o \
	WMAP_9yr_gibbs.o \
	WMAP_9yr_tt_pixlike.o \
	WMAP_9yr_tt_beam_ptsrc_chisq.o \
	WMAP_9yr_teeebb_pixlike.o \
	WMAP_9yr_tetbeebbeb_pixlike.o \
	WMAP_9yr_likelihood.o
#
#			General Commands.
#
DIFF = diff -w
RM = rm -f

# See the CHANGES files for a description of these options
WMAPFLAGS  = -DOPTIMIZE
#WMAPFLAGS += -DUSE_LOWELL_TBEB    # turns on low-l maxlike TB/EB
#WMAPFLAGS += -DUSE_HIGHELL_TB     # turns on high-l master TB
#WMAPFLAGS += -DFASTERTT           # speed up matrix low-l TT
#WMAPFLAGS += -DTIMING             # print out timing stats for profiling

#
#			Compiler/linker configuration.  Several samples
#			are supplied.
#
## SGI IRIX/MIPSpro-- gets the LAPACK functions from the system SCSL library.

#F90    = f90
#FFLAGS = -O -64 $(WMAPFLAGS)
#INCS   = -I. -I$(CFITSIO)/include 
#LIBS   = -L. -L$(CFITSIO)/lib -lcfitsio -lscs_mp

## Linux/Intel compiler and MKL libraries

F90    = ifort
FFLAGS = -O2 -fpic $(WMAPFLAGS) 
INCS   = -I. -I$(CFITSIO)/include
LIBS = -L. -L/usr/site/intel_mkl/lib/em64t -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5 -lmkl_mc3 -lmkl_def -lmkl_lapack -L$(CFITSIO) -lcfitsio

# >>>>>> Note: the options below have not been tested recently. YMMV <<<<<<

## Linux desktop
#LAPACK = -L/usr/site/intelmkl-9.0.018/lib/32 -lmkl_lapack -lmkl -lguide -lpthread
#F90    = ifort
#FFLAGS = -O2 $(WMAPFLAGS) -u -g -O2 -CB -traceback -warn all -warn noerrors \
#-check all -check noarg_temp_created -fpe0 -zero -Vaxlib -fpp
#INCS   = -I. -I$(CFITSIO)/include
#LIBS   = -L. -L$(CFITSIO)/lib -lcfitsio $(LAPACK)

## NAG
#F90	 = f95
#FFLAGS  = -g -O2 -kind=byte -colour $(WMAPFLAGS)
#INCS	 = -I. -I$(CFITSIO)/include -I<lapack path>/include
#LIBS	 = -L. -L$(CFITSIO)/lib -L<lapack path>/lib -llapack -lcfitsio

## MacOS X, G5 hardware
#F90 = <path to compiler>/xlf90 
#FFLAGS  = -qsuffix=f=f90:cpp=F90 -qstrict -qmaxmem=-1 \
#          -qarch=auto -qtune=auto -qunroll=auto -framework Accelerate -O2 \
#          $(WMAPFLAGS)
#INCS = -I. -I$(CFITSIO)/include
#LIBS = -L$(CFITSIO)/lib -lcfitsio -lm -lSystemStubs

## MacOS X, G4 hardware
#F90 = <path to compiler>/xlf90 
#FFLAGS  = -qsuffix=f=f90:cpp=F90 -qstrict -qmaxmem=-1 \
#          -qarch=auto -qtune=auto -qunroll=auto -framework Accelerate -O2 \
#          $(WMAPFLAGS)
#INCS = -I. -I$(CFITSIO)/include
#LIBS = -L$(CFITSIO)/lib -lcfitsio

## PGF90 -- Portland Group compiler.
#F90    = <path to compiler>/pgf90
#FFLAGS = -fast $(WMAPFLAGS)
#INCS   = <-DMPI if using mpi> -I<your mpi path>/include \
#         -I$(CFITSIO)/include
#LIBS   = -L. -L/usr/local/lib -l$(LLIB) \
#         -L<your cfitsio library path>/lib -L<your lapack/blas library path>/lib \
#         -L<other library path>/lib -llapack -lcfitsio -lblas -l<other libraries, e.g. mpi>
#
#			Rules.
#
PROGRAMS = test 

all: $(PROGRAMS) 

check: test
	./test

$(WMAPLIB): $(OBJS)
	ar r $@ $^

%: $(OBJS) %.o
	$(F90) $(FFLAGS) -o $@ $^ $(LIBS)

%.o: %.f90
	$(F90) $(FFLAGS) $(INCS) -c -o $@ $<

%.o: %.F90
	$(F90) $(FFLAGS) $(INCS) -c -o $@ $<

clean:
	$(RM) *.o *.mod *.log *~ *.a 

distclean: clean
	$(RM) *.a $(PROGRAMS)




