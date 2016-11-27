
# Download

##### libdill

```
$ wget http://libdill.org/libdill-0.9-beta.tar.gz
$ tar -xzf libdill-0.9-beta.tar.gz 
$ cd libdill-0.9-beta
$ ./configure
$ make
$ sudo make install
```

**Nov 19, 2016 <http://libdill.org/libdill-0.9-beta.tar.gz>**

* A lot of optimizations. Context switch have been seen to execute in 6ns, coroutine creation in 26ns. Passing a message via a channel in 40ns.
* New `go_stack()` construct allows to run coroutine on a user-allocated stack. 
* New `--enable-census` option monitors coroutines' stack usage and prints thr statistics on process shutdown.
* Mutliple bug fixes.

Oct 16, 2016 <http://libdill.org/libdill-0.8-beta.tar.gz>
Oct 13, 2016 <http://libdill.org/libdill-0.7-beta.tar.gz>
Sep 07, 2016: <http://libdill.org/libdill-0.6-beta.tar.gz>
Jun 03, 2016: <http://libdill.org/libdill-0.5-beta.tar.gz>
May 22, 2016: <http://libdill.org/libdill-0.4-beta.tar.gz>
May 15, 2016: <http://libdill.org/libdill-0.3-beta.tar.gz>

##### dsock 

```
$ wget http://libdill.org/dsock-0.4-alpha.tar.gz
$ tar -xzf dsock-0.4-alpha.tar.gz 
$ cd dsock-0.4-alpha
$ ./configure
$ make
$ sudo make install
```

**Nov 19, 2016  <http://libdill.org/dsock-0.4-alpha.tar.gz>**
Oct 16, 2016  <http://libdill.org/dsock-0.3-alpha.tar.gz>
Aug 13, 2016: <http://libdill.org/dsock-0.2-alpha.tar.gz>
Aug 07, 2016: <http://libdill.org/dsock-0.1-alpha.tar.gz>
