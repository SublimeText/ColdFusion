import sublime, sublime_plugin

completions = []
dotcompletions = {}
dotcompletions["CGI"] = [
    ("AUTH_PASSWORD", "AUTH_PASSWORD"),
    ("AUTH_TYPE", "AUTH_TYPE"),
    ("AUTH_USER", "AUTH_USER"),
    ("CERT_COOKIE", "CERT_COOKIE"),
    ("CERT_FLAGS", "CERT_FLAGS"),
    ("CERT_ISSUER", "CERT_ISSUER"),
    ("CERT_KEYSIZE", "CERT_KEYSIZE"),
    ("CERT_SECRETKEYSIZE", "CERT_SECRETKEYSIZE"),
    ("CERT_SERIALNUMBER", "CERT_SERIALNUMBER"),
    ("CERT_SERVER_ISSUER", "CERT_SERVER_ISSUER"),
    ("CERT_SERVER_SUBJECT", "CERT_SERVER_SUBJECT"),
    ("CERT_SUBJECT", "CERT_SUBJECT"),
    ("CF_TEMPLATE_PATH", "CF_TEMPLATE_PATH"),
    ("CONTENT_LENGTH", "CONTENT_LENGTH"),
    ("CONTENT_TYPE", "CONTENT_TYPE"),
    ("GATEWAY_INTERFACE", "GATEWAY_INTERFACE"),
    ("HTTP_ACCEPT", "HTTP_ACCEPT"),
    ("HTTP_ACCEPT_ENCODING", "HTTP_ACCEPT_ENCODING"),
    ("HTTP_ACCEPT_LANGUAGE", "HTTP_ACCEPT_LANGUAGE"),
    ("HTTP_CONNECTION", "HTTP_CONNECTION"),
    ("HTTP_COOKIE", "HTTP_COOKIE"),
    ("HTTP_HOST", "HTTP_HOST"),
    ("HTTP_USER_AGENT", "HTTP_USER_AGENT"),
    ("HTTP_REFERER", "HTTP_REFERER"),
    ("HTTPS", "HTTPS"),
    ("HTTPS_KEYSIZE", "HTTPS_KEYSIZE"),
    ("HTTPS_SECRETKEYSIZE", "HTTPS_SECRETKEYSIZE"),
    ("HTTPS_SERVER_ISSUER", "HTTPS_SERVER_ISSUER"),
    ("HTTPS_SERVER_SUBJECT", "HTTPS_SERVER_SUBJECT"),
    ("PATH_INFO", "PATH_INFO"),
    ("PATH_TRANSLATED", "PATH_TRANSLATED"),
    ("QUERY_STRING", "QUERY_STRING"),
    ("REMOTE_ADDR", "REMOTE_ADDR"),
    ("REMOTE_HOST", "REMOTE_HOST"),
    ("REMOTE_USER", "REMOTE_USER"),
    ("REQUEST_METHOD", "REQUEST_METHOD"),
    ("SCRIPT_NAME", "SCRIPT_NAME"),
    ("SERVER_NAME", "SERVER_NAME"),
    ("SERVER_PORT", "SERVER_PORT"),
    ("SERVER_PORT_SECURE", "SERVER_PORT_SECURE"),
    ("SERVER_PROTOCOL", "SERVER_PROTOCOL"),
    ("SERVER_SOFTWARE", "SERVER_SOFTWARE"),
    ("WEB_SERVER_API", "WEB_SERVER_API"),
    ("CONTEXT_PATH", "CONTEXT_PATH"),
    ("LOCAL_ADDR", "LOCAL_ADDR"),
    ("LOCAL_HOST", "LOCAL_HOST")
]

class DotCompletionsCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        sel = self.view.sel()[0]

        # insert the actual . character
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ".")

        if self.view.settings().get("auto_complete") == False:
            return

        word = self.view.word(sel.begin() - 1)
        if self.view.substr(word) == "CGI":
            completions.extend(dotcompletions["CGI"])
            t = self.view.settings().get("auto_complete_delay")
            sublime.set_timeout(lambda:
                    self.view.run_command("auto_complete", {
                                        'disable_auto_insert': True,
                                        'next_completion_if_showing': False,
                                        'api_completions_only': True}), t)

class OnDotCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        _completions = []
        _completions.extend(completions)

        del completions[:]
        return _completions


