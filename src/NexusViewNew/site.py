from html import escape
from IPython.display import HTML, display
import urllib.request
from NexusViewNew.custom_exception import InvalidURLException
from NexusViewNew.logger import logger



def is_valid(URL: str) -> bool:
    try:
        response_status = urllib.request.urlopen(URL).getcode()
        assert response_status == 200
        logger.debug(f"response_status: {response_status}")
        return True
    except Exception as e:
        logger.exception(e)
        return False
    

def render_site(URL: str, width: str = "100%", height: str = "600") -> str:
    try:
        if is_valid(URL):
            iframe = f"""
            <iframe
                src="{escape(URL, quote=True)}"
                width="{escape(str(width), quote=True)}"
                height="{escape(str(height), quote=True)}"
                frameborder="0"
                allowfullscreen>
            </iframe>
            """
            display(HTML(iframe))
            return "success"
        else:
            raise InvalidURLException
    except Exception as e:
        raise e
