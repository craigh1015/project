from operator import itemgetter

import model


def setup_function():
    model.clear()


def test_empty():
    assert ([], True) == model.getTasks()


def test_add():
    assert True == model.add({'id': '0', 'msg': 'test-0'})
    assert ([{'id': '0', 'msg': 'test-0'}], True) == model.getTasks()


def test_add_multiple():
    assert True == model.add({'id': '0', 'msg': 'test-0'})
    assert True == model.add({'id': '1', 'msg': 'test-1'})
    (tasks, success) = model.getTasks()
    assert [{'id': '0', 'msg': 'test-0'}, {'id': '1', 'msg': 'test-1'}
            ] == sorted(tasks, key=itemgetter('id'))
    assert success == True


def test_delete():
    assert True == model.add({'id': '0', 'msg': 'test-0'})
    assert True == model.add({'id': '1', 'msg': 'test-1'})
    model.delete('1')
    assert ([{'id': '0', 'msg': 'test-0'}], True) == model.getTasks()


def test_delete_missing():
    assert True == model.add({'id': '0', 'msg': 'test-0'})
    model.delete('1')
    assert ([{'id': '0', 'msg': 'test-0'}], True) == model.getTasks()


def test_update():
    assert True == model.add({'id': '0', 'msg': 'test-0'})
    model.update({'id': '0', 'msg': 'test-0 updated', 'msg2': 'New message'})
    assert ([{'id': '0', 'msg': 'test-0 updated',
              'msg2': 'New message'}], True) == model.getTasks()


def test_update_missing():
    model.update({'id': '0', 'msg': 'test-0 updated', 'msg2': 'New message'})
    assert ([{'id': '0', 'msg': 'test-0 updated',
              'msg2': 'New message'}], True) == model.getTasks()


def test_add_duplicate():
    assert True == model.add({'id': '0', 'msg': 'test-0 first'})
    assert False == model.add({'id': '0', 'msg': 'test-0 second'})
    (tasks, success) = model.getTasks()
    assert [{'id': '0', 'msg': 'test-0 first'}
            ] == sorted(tasks, key=itemgetter('id'))
    assert success == True
