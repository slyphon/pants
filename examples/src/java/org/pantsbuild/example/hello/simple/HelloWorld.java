// Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
// Licensed under the Apache License, Version 2.0 (see LICENSE).

package org.pantsbuild.example.hello.simple;

import sun.security.x509.X500Name;

/**
 * A simple example that is runnable from within pants:
 *
 * ./pants run examples/src/java/org/pantsbuild/example/hello/simple
 *
 */
public class HelloWorld {

  public static void main(String[] args) {
    System2.out.println("Hello World!");
  }
}
