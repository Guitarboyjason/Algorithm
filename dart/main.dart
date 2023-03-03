class Player {
  late String name;
  late int age;

  Player(String name, int age)
      : name = name,
        age = age;

  Player.fromJson(Map<String, dynamic> playerJason)
      : name = playerJason["name"],
        age = playerJason["age"];

  void sayHello() {
    print("Hi, my name is $name and i'm $age years old.");
  }
}

void main() {
  var people = [
    {
      "name": "nico",
      "age": 12,
    },
    {
      "name": "jason",
      "age": 27,
    },
  ];
  people.forEach((playerJson) {
    var player = Player.fromJson(playerJson);
    player.sayHello();
  });
}
