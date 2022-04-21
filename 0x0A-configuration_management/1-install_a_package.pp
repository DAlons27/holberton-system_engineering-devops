#install puppet-lint
package { 'puppet_lint':
    ensure   => '2.1.0',
    name     => 'puppet-lint',
    provider => 'gem',
    source   => 'http://rubygems.org',
}