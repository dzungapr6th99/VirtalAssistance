English content is below:

Vietnamese Content:
Dự án này mình dự định làm 1 con Q/A để tiếp quản 1 project. Bài toán đặt ra như sau: 
- Khi team khởi động 1 dự án, với công ty quy mô nhỏ sẽ hay làm mô hình như sau:
     * Leader của team sẽ lên kế hoạch kiến trúc hệ thống, quy chuẩn code. (Ở đây mình lấy luôn chuẩn code solid)
     * Dự án dài hơi thì việc mấy ông loi choi nghỉ ngang là chuyện đương nhiên, người mới vào => cần ông leader training => có thể mất thời gian ông leader (lương ông leader 50tr - 60tr, tự dưng mất cả buổi chỉ để chỉ việc cho thằng lương 15tr 20tr).
     * Chẳng may có gì hệ trọng, ô leader bị dí/ ốm, thì thằng người mới có thể hết người hỏi. 
     * Ông leader mà nhảy việc, 1 ông khác vào làm leader. chẳng may có vấn đề gì đó phức tạp, không biết hỏi ai đành phải tự mò
- Hướng giải quyết vấn đề:
     * Bây giờ có 1 con AI tiếp nhận tri thức của cả dự án, làm 1 còn Q/A Service
     * Tuy nhiên RAG cả đống dự án vào, cả tài liệu, code thì không 1 con Model LLM nào nó cân được vì câu chuyên muôn thuở là ngữ cảnh
     * Nhưng mà bóc tách vấn đề nhỏ ra, cung cấp từng thông tin cần thiết thì mấy con đó lại trả lời được.

Sau khi tham khảo nhiều nguồn thì quyết dùng Milvus, Neo4J, Ollama để tạo 1 con Q/A service. sẽ làm theo tương tự bootcamp của Zilliz như link này https://github.com/milvus-io/bootcamp. và mình thay đổi cụ thể cái Node của nó cho phù hợp hơn bài toán:

Cấu trúc Node trong graph:
  - FileName: tên file(bao gồm cả đường dẫn, tên file)
  - Type: là code hay là documents?
  - Module: Cái file này nó đang mô tả/ impplements cho chức năng nào
  - Content: nội dung của Chunk

English content:
In this project, I will develop a Q/A service with purpose is take over the tech project. The problem posed:
  - With medium and small technology company, when they start a tech project, liked my first company, they would implement like below:
     *  Team's leader will plan for software architecture, coding convention (In this project, I only solved for the code which follow SOLID principles)
     *  During implement project, job hoping of lower employee is unavoidable. The new one join => need the leader training => time consuming for the leader (Salary of leader 2k - 3k but must training for the fresher and fresher's salary is 600 - 800$)
     *  Some time, leader is "pressing" (reported bug, fix bug, ...), or sick, the fresher have no ones to ask => maybe fresher free whole time at that day.
     *  Worse is leader jumping jobs => the new leaders can not take over all the issue
  - My solving problem:
     * Building an AI can take over the project. I will build a Q/A service
     * But you can RAG whole project. the challenge of all LLM now is context.
     * But if you provide enough data(not all data), It still answer correctly. Now how to provide enough data automatic? The solution is a service an find relevant information.
After referenct many source in internet, I decide use Milvus, Neo4J and Ollama, follow this bootcamp link of Zilliz https://github.com/milvus-io/bootcamp. But I change the Node to suit with my problem.

Architecture of graph:
-  FileName: Name of file (include path, link, name of file)
-  Type: is Code or Document?
-  Module: Which is the Document is descript for or the code is implement for?
-  Content: the content of the chunk

