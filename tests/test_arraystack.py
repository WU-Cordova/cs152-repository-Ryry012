import pytest
from datastructures.arraystack import ArrayStack

# Test cases for ArrayStack
def test_push():
    stack = ArrayStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_pop_empty():
    stack = ArrayStack(3)
    with pytest.raises(ValueError):
        stack.pop()

def test_peek_empty():
    stack = ArrayStack(3)
    with pytest.raises(ValueError):
        stack.peek()

def test_is_empty():
    stack = ArrayStack(3)
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

def test_is_full():
    stack = ArrayStack(3)
    assert stack.is_full() is False
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.is_full() is True

def test_clear():
    stack = ArrayStack(3)
    stack.push(1)
    stack.push(2)
    stack.clear()
    assert stack.is_empty() is True

def test_contains():
    stack = ArrayStack(3)
    stack.push(1)
    stack.push(2)
    assert 1 in stack
    assert 2 in stack
    assert 3 not in stack

def test_eq():
    stack1 = ArrayStack(3)
    stack1.push(1)
    stack1.push(2)

    stack2 = ArrayStack(3)
    stack2.push(1)
    stack2.push(2)

    assert stack1 == stack2
