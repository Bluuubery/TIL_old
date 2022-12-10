package java08;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class hashmap {
    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<>();
        map.put("스쿼트", "하체");
        map.put("벤치프레스", "가슴");

        System.out.println(map.keySet());

        List<String> keyList = new ArrayList<>(map.keySet());
        
        System.out.println(keyList);
        // System.out.println(map.get("스쿼트"));
        // System.out.println(map.getOrDefault("데드리프트", "헬스"));

        // System.out.println(map.containsKey("스쿼트"));
        // System.out.println(map.remove("벤치프레스"));

    }
}
