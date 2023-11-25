#!/bin/sh
alias nohm='bwrap --dev-bind / / --ro-bind /dev/null /etc/ld.so.preload';
alias gethmlogs='sudo journalctl -ball | grep -i -e hardened_malloc -e "fatal allocator error"';
