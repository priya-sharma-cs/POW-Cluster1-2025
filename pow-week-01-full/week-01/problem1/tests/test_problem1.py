from solution_1 import Node, count_unival_subtrees, build_sample_tree
from solution_2 import Node as Node2, count_unival_subtrees_naive, build_sample_tree as build_sample_tree2

def test_sample():
    root = build_sample_tree()
    assert count_unival_subtrees(root) == 5

def test_sample_naive():
    root = build_sample_tree2()
    assert count_unival_subtrees_naive(root) == 5

def test_empty():
    assert count_unival_subtrees(None) == 0
    assert count_unival_subtrees_naive(None) == 0

def test_single():
    n = Node(7)
    assert count_unival_subtrees(n) == 1
