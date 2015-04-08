

from osp.citations.hlom.models.citation import HLOM_Citation
from osp.citations.hlom.network import Network


def test_build(models, add_hlom, add_doc):

    # 5 HLOM texts.
    t1 = add_hlom(control_number='cn1', title='title1', author='author1')
    t2 = add_hlom(control_number='cn2', title='title2', author='author2')
    t3 = add_hlom(control_number='cn3', title='title3', author='author3')

    # 1 syllabus.
    s = add_doc('syllabus')

    # Citations for texts 1 and 2.
    HLOM_Citation.create(document=s, record=t1)
    HLOM_Citation.create(document=s, record=t2)

    n = Network()
    n.add_nodes()

    assert n.graph.node['cn1'] == {
        'title': 'title1', 'author': 'author1'
    }
    assert n.graph.node['cn2'] == {
        'title': 'title2', 'author': 'author2'
    }