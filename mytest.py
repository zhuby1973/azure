from playwright import sync_playwright

def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://portal.azure.com/#home
    page.goto("https://portal.azure.com/#home")

    # Go to https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&response_type=code%20id_token&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile&state=OpenIdConnect.AuthenticationProperties%3DMKbcSxSTICoJN1kt8D5nwvx9SQt4QkVloIDY3FogjShP6o_PQ6ehfTftIxtWpZPXMegc0nuD_uimxQ_93rRQuyPH_xyF-LYgzMBHonwKVldvLp8FCf-DIdApaWzkSRDl2V2-tzUHgSev-RcYdWHOYLak9wMqKlz1XhkgN2FN6dA-gqypCUwK56oYuxxpJhYAnqr17qKSf_SCHhJfc7_knLGbJuxMbwnPsTlc4eep8JEsQALkDnm-x3uIp0leonCFdT95bg8k0PEm0nw0YTUtfelqU90AMvtrW87J4njKceFydEE48q4ecTfSduLK-lnm2bsJ2jlNjfbe16fPD4_2n0kkoDc3nj_26Xvadyk78mtjDn0AAelkC3h_JwLdOwQk&response_mode=form_post&nonce=637426179104629098.Mzc3MjE4MjQtZGUzZC00ZjdlLWJkZjEtMDljNzhmNjljM2NlMjczNmQ3MDctZWM1My00YmYzLTg0NzktNWYzYTIyNzdmY2Qy&redirect_uri=https%3A%2F%2Fportal.azure.com%2Fsignin%2Findex%2F&site_id=501430&client-request-id=d9c101d6-d381-4640-a8af-7b643cee945d&x-client-SKU=ID_NET45&x-client-ver=5.3.0.0
    page.goto("https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&response_type=code%20id_token&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile&state=OpenIdConnect.AuthenticationProperties%3DMKbcSxSTICoJN1kt8D5nwvx9SQt4QkVloIDY3FogjShP6o_PQ6ehfTftIxtWpZPXMegc0nuD_uimxQ_93rRQuyPH_xyF-LYgzMBHonwKVldvLp8FCf-DIdApaWzkSRDl2V2-tzUHgSev-RcYdWHOYLak9wMqKlz1XhkgN2FN6dA-gqypCUwK56oYuxxpJhYAnqr17qKSf_SCHhJfc7_knLGbJuxMbwnPsTlc4eep8JEsQALkDnm-x3uIp0leonCFdT95bg8k0PEm0nw0YTUtfelqU90AMvtrW87J4njKceFydEE48q4ecTfSduLK-lnm2bsJ2jlNjfbe16fPD4_2n0kkoDc3nj_26Xvadyk78mtjDn0AAelkC3h_JwLdOwQk&response_mode=form_post&nonce=637426179104629098.Mzc3MjE4MjQtZGUzZC00ZjdlLWJkZjEtMDljNzhmNjljM2NlMjczNmQ3MDctZWM1My00YmYzLTg0NzktNWYzYTIyNzdmY2Qy&redirect_uri=https%3A%2F%2Fportal.azure.com%2Fsignin%2Findex%2F&site_id=501430&client-request-id=d9c101d6-d381-4640-a8af-7b643cee945d&x-client-SKU=ID_NET45&x-client-ver=5.3.0.0")

    # Click text="Email, phone, or Skype"
    page.click("text=\"Email, phone, or Skype\"")

    # Fill input[aria-label="Enter your email, phone, or Skype."]
    page.fill("input[aria-label=\"Enter your email, phone, or Skype.\"]", "hacker2okb@OTAPRD1485ops.onmicrosoft.com")

    # Click input[type="submit"]
    # with page.expect_navigation(url="https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&response_type=code%20id_token&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile&state=OpenIdConnect.AuthenticationProperties%3DMKbcSxSTICoJN1kt8D5nwvx9SQt4QkVloIDY3FogjShP6o_PQ6ehfTftIxtWpZPXMegc0nuD_uimxQ_93rRQuyPH_xyF-LYgzMBHonwKVldvLp8FCf-DIdApaWzkSRDl2V2-tzUHgSev-RcYdWHOYLak9wMqKlz1XhkgN2FN6dA-gqypCUwK56oYuxxpJhYAnqr17qKSf_SCHhJfc7_knLGbJuxMbwnPsTlc4eep8JEsQALkDnm-x3uIp0leonCFdT95bg8k0PEm0nw0YTUtfelqU90AMvtrW87J4njKceFydEE48q4ecTfSduLK-lnm2bsJ2jlNjfbe16fPD4_2n0kkoDc3nj_26Xvadyk78mtjDn0AAelkC3h_JwLdOwQk&response_mode=form_post&nonce=637426179104629098.Mzc3MjE4MjQtZGUzZC00ZjdlLWJkZjEtMDljNzhmNjljM2NlMjczNmQ3MDctZWM1My00YmYzLTg0NzktNWYzYTIyNzdmY2Qy&redirect_uri=https%3A%2F%2Fportal.azure.com%2Fsignin%2Findex%2F&site_id=501430&client-request-id=d9c101d6-d381-4640-a8af-7b643cee945d&x-client-SKU=ID_NET45&x-client-ver=5.3.0.0"):
    with page.expect_navigation():
        page.click("input[type=\"submit\"]")

    # Click text="Password"
    page.click("text=\"Password\"")

    # Fill input[aria-label="Enter the password for hacker2okb@otaprd1485ops.onmicrosoft.com"]
    page.fill("input[aria-label=\"Enter the password for hacker2okb@otaprd1485ops.onmicrosoft.com\"]", "QZiO$*CTQPQ5")

    # Click input[type="submit"]
    # with page.expect_navigation(url="https://login.microsoftonline.com/common/login"):
    with page.expect_navigation():
        page.click("input[type=\"submit\"]")

    # Click input[type="submit"]
    # with page.expect_navigation(url="https://portal.azure.com/#home"):
    with page.expect_navigation():
        page.click("input[type=\"submit\"]")

    # Click text="Virtual machines"
    page.click("text=\"Virtual machines\"")
    # assert page.url() == "https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Compute%2FVirtualMachines"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
