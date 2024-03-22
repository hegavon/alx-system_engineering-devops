#!/usr/bin/pup
# Define a package resource for installing Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}