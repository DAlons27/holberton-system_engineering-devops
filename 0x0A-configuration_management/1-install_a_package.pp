#install puppet-lint
package { 'puppet_lint':
    ensure   => '2.5.0',
    provider => 'gem',
    source   => 'https://rubygems.org',
}