class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  } // if current.next = node, current =
}
class LinkedList {
  constructor(data) {
    this.head = data;
  }
  append(data) {
    let node = new Node(data);
    if (!this.head) {
      // 1st is always "head" and "node" must be "head"
      this.head = node;
    } else {
      let current = this.head; // later "head" will be "current" for sure |current = this.head
      while (current.next) {
        // if "head" becomes "current", "current.next" becomes current. | current = current.next
        current = current.next;
      }
      current.next = node; //Always first is "head" and "head" is "node" and list is "current.next" and its node
    }
  }

  print() {
    let current = this.head,
      result = "";
    while (current) {
      result += current.data + (current.next ? ">" : "");
      current = current.next;
    }
    console.log(result);
  }
}

let list = new LinkedList();
list.append(0);
list.append(1);
list.append(2);
list.append(3);
list.print();
