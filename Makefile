NAME = fonts
rpmsourcedir = /tmp/$(shell whoami)/rpmbuild

rpm:
	mkdir -p $(rpmsourcedir) ; \
	tar -C ../ -cf $(rpmsourcedir)/smartmet-$(NAME).tar $(NAME) ; \
	gzip -f $(rpmsourcedir)/smartmet-$(NAME).tar ; \
        TAR_OPTIONS=--wildcards rpmbuild -v -ta $(rpmsourcedir)/smartmet-$(NAME).tar.gz
