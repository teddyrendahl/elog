import pytest
import os.path
import logging

from elog.pswww import PHPWebService


logger = logging.getLogger(__name__)

# Used for simulated post
image_png = os.path.join(os.path.dirname(__file__), 'lenna.png')

msg = """\
This is an automated test of https://github.com/pcdshub/elog
"""


@pytest.mark.unit
def test_pswww_notebooks(pswww):
    logger.debug('test_pswww_notebooks')
    assert pswww.get_facilities_logbook('SXR Instrument') == '46'
    assert isinstance(pswww.get_experiment_logbook('SXR'), str)


@pytest.mark.post
def test_pswww_post_smoke():
    logger.debug('test_pswww_post_smoke')
    pswww = PHPWebService()
    pswww.post(msg, '302', tags=['test'],
               attachments=[(image_png, 'Canonical test image "Lenna"'),
                            image_png])
