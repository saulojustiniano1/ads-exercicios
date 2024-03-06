class NavegacaoWeb:
    def __init__(self):
        self.site = []

    def abrir_link(self, site):
        self.site.append(site)
        print(f"Site {site} foi aberta.")
        print(25 * "-")

    def voltar_link(self):
        self.site.pop()

    def exibir_links(self):
        print("Sites abertos:")
        for site in self.site:
            if site != self.site[-1]:
                print(site, end=" - ")
            if site == self.site[-1]:
                print(f"{site} (ATUAL)")

        print(25 * "-")


web = NavegacaoWeb()

web.abrir_link("Google")
web.abrir_link("Facebook")
web.abrir_link("Youtube")
web.abrir_link("Twitter")

web.exibir_links()
web.voltar_link()
web.exibir_links()
