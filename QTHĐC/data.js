const managementQuizData = [
  {
    id: 17,
    question: "Sau quá trình kiểm tra, khi nào thì nhà quản lý không cần thực hiện các điều chỉnh?",
    options: {
      a: "khi nguyên nhân của sự thay đổi đã được xác định",
      b: "khi tiêu chuẩn được chấp nhận",
      c: "khi tiêu chuẩn không được chấp nhận",
      d: "khi độ sai lệch có thể chấp nhận được"
    },
    answer: "d"
  },
  {
    id: 18,
    question: "Ủy quyền đảm bảo nguyên tắc về tính tuyệt đối trong trách nhiệm:",
    options: {
      a: "Cấp dưới dám ra quyết định và chịu trách nhiệm chứ không đùn đẩy lại nhiệm vụ cho cấp trên",
      b: "Cấp dưới chịu trách nhiệm hoàn toàn, cấp trên không liên quan",
      c: "Cấp trên chịu trách nhiệm và ra quyết định hết",
      d: "Cấp dưới tuyệt đối tuân thủ và không ra quyết định"
    },
    answer: "a"
  },
  {
    id: 19,
    question: "Phát biểu nào sau đây là đúng khi ứng dụng thuyết hai yếu tố của Herzberg vào thực tiễn quản trị?",
    options: {
      a: "Lương bổng vừa là yếu tố duy trì, vừa là yếu tố động viên",
      b: "Chính sách và quy định quản lý của tổ chức thuộc nhóm yếu tố động viên",
      c: "Cả a và b đều đúng",
      d: "Cả a và b đều sai"
    },
    answer: "a"
  },
  {
    id: 20,
    question: "Phát biểu nào sau đây không đúng trong một tổ chức:",
    options: {
      a: "Cấp bậc quản trị càng cao thì kỹ năng tư duy càng cần phải cao",
      b: "Cấp bậc quản trị càng cao thì kỹ năng kỹ thuật càng giảm dần tính quan trọng",
      c: "Các nhà quản trị cấp trung cần có kỹ năng quan hệ cao hơn các nhà quản trị cấp cao và cấp cơ sở",
      d: "Các nhà quản trị cấp cơ sở cần thiết phải có kỹ năng kỹ thuật, chuyên môn cao hơn các nhà quản trị cấp cao và cấp trung"
    },
    answer: "c"
  },
  {
    id: 21,
    question: "Trong bốn chức năng cơ bản của quản trị, Quản trị viên cấp cao dành nhiều thời gian nhất để thực hiện chức năng quản trị nào?",
    options: {
      a: "Lập kế hoạch",
      b: "Lãnh đạo",
      c: "Tổ chức",
      d: "Kiểm tra"
    },
    answer: "a"
  },
  {
    id: 22,
    question: "Phong cách lãnh đạo nào sau đây mô tả một người lãnh đạo trao cho các thành viên trong nhóm tự do hoàn toàn để ra quyết định và hoàn thành công việc theo cách thức họ cảm thấy phù hợp nhất?",
    options: {
      a: "Phong cách tự do",
      b: "Phong cách độc đoán",
      c: "Phong cách văn hóa",
      d: "Phong cách dân chủ"
    },
    answer: "a"
  },
  {
    id: 23,
    question: "Hoạt động quản trị cần thiết vì:",
    options: {
      a: "Thể hiện người quản trị cấp cao là quan trọng nhất",
      b: "Thể hiện người quản trị cấp thấp luôn có năng lực thấp hơn người quản trị cấp cao",
      c: "Cho thấy sự phân chia cấp bậc rõ ràng",
      d: "Đảm bảo cho việc sử dụng các yếu tố nguồn lực có hiệu quả nhất"
    },
    answer: "d"
  },
  {
    id: 24,
    question: "Với cùng số lượng nhân viên thì:",
    options: {
      a: "Khi tầm hạn quản trị giảm, số cấp quản trị giảm",
      b: "Khi tầm hạn quản trị giảm, số cấp quản trị tăng",
      c: "Khi tầm hạn quản trị tăng, công việc sẽ tăng",
      d: "Không câu nào đúng"
    },
    answer: "b"
  },
  {
    id: 25,
    question: "Các biện pháp được áp dụng trong quá trình thực hiện mục tiêu chiến lược nhằm tác động đến các đối tượng liên quan được gọi là:",
    options: {
      a: "Thủ tục",
      b: "Chiến lược",
      c: "Chính sách",
      d: "Quy trình"
    },
    answer: "c"
  },
  {
    id: 26,
    question: "Long là trưởng phòng an ninh của một Ban Quản lý chung cư... Phong cách lãnh đạo của Long là:",
    options: {
      a: "Phong cách tự do",
      b: "Phong cách chú trọng đến con người",
      c: "Phong cách dân chủ",
      d: "Phong cách chuyên quyền"
    },
    answer: "c"
  },
  {
    id: 27,
    question: "Người lãnh đạo luôn tạo ra các cơ hội để nhân viên phát huy khả năng... Điều này nhằm đáp ứng nhu cầu:",
    options: {
      a: "Nhu cầu an toàn",
      b: "Nhu cầu được tôn trọng",
      c: "Nhu cầu xã hội",
      d: "Nhu cầu thể hiện bản thân"
    },
    answer: "d"
  },
  {
    id: 28,
    question: "Ba sự khác biệt giữa các kế hoạch chiến lược và kế hoạch tác nghiệp là:",
    options: {
      a: "Nhóm các mục tiêu đã được xác định, chi phí, số lượng người tham gia lập kế hoạch",
      b: "Khung thời gian, chi phí, tuổi thọ của tổ chức",
      c: "Chi phí, tuổi thọ của tổ chức, số lượng người tham gia lập kế hoạch",
      d: "Phạm vi, khung thời gian, nhóm các mục tiêu đã được xác định"
    },
    answer: "d"
  },
  {
    id: 29,
    question: "Một hệ thống mà không chịu tác động của môi trường được gọi là hệ thống:",
    options: {
      a: "Hoạt động",
      b: "Đóng",
      c: "Mở",
      d: "Phụ"
    },
    answer: "b"
  },
  {
    id: 30,
    question: "Nội dung nào sau đây thuộc chức năng lãnh đạo:",
    options: {
      a: "Phong cách lãnh đạo",
      b: "Phương pháp lãnh đạo",
      c: "Tất cả các phương án trên đều đúng",
      d: "Nhận thức đúng về các yếu tố con người trong tổ chức"
    },
    answer: "c"
  },
  {
    id: 31,
    question: "Quang muốn chuyển quyền hành và trách nhiệm của mình cho cấp dưới. Quá trình này được gọi là:",
    options: {
      a: "Ủy quyền",
      b: "Chuyên môn hóa bộ phận",
      c: "Phối hợp",
      d: "Trách nhiệm giải trình"
    },
    answer: "a"
  },
  {
    id: 32,
    question: "Các kế hoạch được áp dụng cho toàn bộ tổ chức... được gọi là kế hoạch gì?",
    options: {
      a: "Kế hoạch chiến lược",
      b: "Kế hoạch tác nghiệp",
      c: "Kế hoạch ngắn hạn",
      d: "Kế hoạch cụ thể"
    },
    answer: "a"
  },
  {
    id: 33,
    question: "Một tổ chức được hiểu là:",
    options: {
      a: "Một tập hợp của hai hay nhiều người cùng hoạt động trong những hình thái cơ cấu nhất định để đạt được các mục tiêu chung.",
      b: "Một nhóm các các nhân tập trung vào lợi nhuận mang lại cho các cổ đông của họ.",
      c: "Một tập hợp các cá nhân cùng làm việc trong một công ty.",
      d: "Một địa điểm cụ thể nơi mọi thành viên làm việc."
    },
    answer: "a"
  },
  {
    id: 34,
    question: "Trong bốn chức năng cơ bản của quản trị, Quản trị viên cấp cơ sở dành nhiều thời gian nhất để thực hiện chức năng quản trị nào?",
    options: {
      a: "Lãnh đạo",
      b: "Tất cả các chức năng trên",
      c: "Lập kế hoạch",
      d: "Tổ chức và kiểm tra"
    },
    answer: "a"
  },
  {
    id: 35,
    question: "Xây dựng ngân quỹ là khi người quản lý:",
    options: {
      a: "Xác định số tiền cần huy động để thực hiện dự án",
      b: "Xác định mục tiêu của kế hoạch",
      c: "Xây dựng phương án phụ trợ",
      d: "Tất cả các phương án trên sai"
    },
    answer: "a"
  },
  {
    id: 36,
    question: "Kế hoạch tác nghiệp có xu hướng tập trung vào:",
    options: {
      a: "Những vấn đề hàng ngày và cụ thể",
      b: "Tương lai dài hạn của tổ chức",
      c: "Định hướng hoạt động của tổ chức",
      d: "Vị thế của tổ chức trên thị trường"
    },
    answer: "a"
  },
  {
    id: 37,
    question: "Hình thức nhà quản trị đo lường/ đánh giá công việc thực tế của nhân viên gần giống với hình thức mà giáo viên..... :",
    options: {
      a: "cho điểm bài kiểm tra",
      b: "giúp sinh viên chuẩn bị cho bài kiểm tra",
      c: "soạn bài kiểm tra",
      d: "chuẩn bị bài tập"
    },
    answer: "a"
  },
  {
    id: 38,
    question: "Theo thuyết hai yếu tố của Herzberg, yếu tố nào sau đây KHÔNG phải yếu tố động viên?",
    options: {
      a: "Sự giám sát",
      b: "Bản thân công việc",
      c: "Sự công nhận",
      d: "Cơ hội phát triển"
    },
    answer: "a"
  },
  {
    id: 39,
    question: "Tất cả các nhà quản trị cần có các kỹ năng:",
    options: {
      a: "Quan hệ con người",
      b: "Tư duy (Nhận thức + thiết kế)",
      c: "Tất cả những câu trên",
      d: "Kỹ thuật"
    },
    answer: "c"
  },
  {
    id: 40,
    question: "...........thường được áp dụng đối với các doanh nghiệp có tính đặc thù cao...:",
    options: {
      a: "Cơ cấu trực tuyến tham mưu",
      b: "Cơ cấu trực tuyến - chức năng",
      c: "Cơ cấu kiểu dự án",
      d: "Cơ cấu kiểu ma trận"
    },
    answer: "c"
  },
  {
    id: 41,
    question: "Xu thế quản lý trên thế giới hiện nay là:",
    options: {
      a: "Giảm tầm hạn quản trị, tăng số cấp quản trị",
      b: "Tăng tầm hạn quản trị, tăng số cấp quản trị",
      c: "Giảm tầm hạn quản trị, giảm số cấp quản trị",
      d: "Tăng tầm hạn quản trị, giảm số cấp quản trị"
    },
    answer: "d"
  },
  {
    id: 42,
    question: ".....trong đó bộ máy quản lý được xây dựng sao cho các tuyến quyền lực trong doanh nghiệp là các đường thẳng...:",
    options: {
      a: "Cơ cấu tổ chức theo kiểu trực tuyến",
      b: "Cơ cấu tổ chức theo kiểu ma trận",
      c: "Cơ cấu tổ chức theo kiểu dự án",
      d: "Cơ cấu tổ chức theo kiểu chức năng"
    },
    answer: "a"
  },
  {
    id: 43,
    question: "Quá trình tác động của người quản lý đến các nhân viên sao cho họ thực sự sẵn sàng... là chức năng nào sau đây:",
    options: {
      a: "Lãnh đạo",
      b: "Kiểm tra",
      c: "Tổ chức",
      d: "Lập kế hoạch"
    },
    answer: "a"
  },
  {
    id: 44,
    question: "Khi một gói ngân sách được sử dụng để kiểm soát, nó cung cấp ..... để so sánh mức sử dụng các nguồn lực:",
    options: {
      a: "tiêu chuẩn linh hoạt",
      b: "tiêu chuẩn định tính",
      c: "tiêu chuẩn định lượng",
      d: "tiêu chuẩn phi ngân quỹ"
    },
    answer: "c"
  },
  {
    id: 45,
    question: "Cơ cấu tổ chức nào sau đây được áp dụng phổ biến trong các doanh nghiệp Việt Nam hiện nay:",
    options: {
      a: "Cơ cấu kiểu ma trận",
      b: "Cơ cấu kiểu trực tuyến tham mưu",
      c: "Cơ cấu kiểu trực tuyến - chức năng",
      d: "Cơ cấu kiểu trực tuyến"
    },
    answer: "c"
  },
  {
    id: 46,
    question: "Cơ cấu tổ chức nào sau đây được áp dụng phổ biến trong các doanh nghiệp Việt Nam hiện nay:",
    options: {
      a: "Cơ cấu kiểu trực tuyến tham mưu",
      b: "Cơ cấu kiểu trực tuyến - chức năng",
      c: "Cơ cấu kiểu ma trận",
      d: "Cơ cấu kiểu trực tuyến"
    },
    answer: "b"
  },
  {
    id: 47,
    question: "Bản chất của hoạt động quản trị là:",
    options: {
      a: "Tất cả các trên",
      b: "Giúp tránh lãng phí các nguồn lực của tổ chức",
      c: "Giúp tổ chức đạt được kết quả với hiệu suất cao thông qua việc sử dụng các nguồn lực hạn chế của tổ chức",
      d: "Giúp tổ chức tiết kiệm chi phí"
    },
    answer: "c"
  },
  {
    id: 48,
    question: "Lãnh đạo tìm cách....... đến người khác để đạt được mục tiêu của tổ chức",
    options: {
      a: "Gây ảnh hưởng",
      b: "Tác động",
      c: "Ra lệnh",
      d: "Bắt buộc"
    },
    answer: "a"
  },
  {
    id: 49,
    question: "Phương pháp giáo dục cho nhân viên về truyền thống uy tín của doanh nghiệp... là phương pháp lãnh đạo nào?",
    options: {
      a: "Kinh tế",
      b: "Giáo dục",
      c: "Tham mưu",
      d: "Hành chính"
    },
    answer: "b"
  },
  {
    id: 50,
    question: "Câu trả lời nào dưới đây là ví dụ về mục tiêu được xây dựng tốt",
    options: {
      a: "Mở rộng thị trường ra nước ngoài",
      b: "Doanh thu đạt 50 tỷ đồng",
      c: "Lợi nhuận tăng rõ rệt",
      d: "Không có phương án trả lời đúng"
    },
    answer: "b"
  }

];

