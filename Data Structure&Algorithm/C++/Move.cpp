#include <iostream>
#include <cstring>
using namespace std;
class MemoryBlock
{
public:
    MemoryBlock(const unsigned int nSize)
    {
        cout << "创建对象，申请内存资源" << nSize << "字节" << endl;
        m_nSize = nSize;
        m_pData = new char[m_nSize];
    }
    ~MemoryBlock()
    {
        cout << "销毁对象";
        if (0 != m_nSize)
        {
            cout << "，释放内存资源" << m_nSize << "字节";
            delete[] m_pData;
            m_nSize = 0;
        }
        cout << endl;
    }
    MemoryBlock(MemoryBlock &&other)
    {
        cout << "移动资源2" << other.m_nSize << "字节" << endl;
        // 将目标对象的内存资源指针直接指向源对象的内存资源
        // 表示将源对象内存资源的管理权移交给目标对象
        m_pData = other.m_pData;
        m_nSize = other.m_nSize; // 复制相应的内存块大小
                                 // 将源对象的内存资源指针设置为nullptr
        // 表示这块内存资源已经归目标对象所有
        // 源对象不再拥有其管理权
        other.m_pData = nullptr;
        other.m_nSize = 0; // 内存块大小设置为0
    }
    // MemoryBlock &operator=(const MemoryBlock &other)
    // {
    //     if (this == &other)
    //     {
    //         return *this;
    //     }
    //     cout << "释放已有内存资源" << m_nSize << "字节" << endl;
    //     delete[] m_pData;
    //     m_nSize = other.GetSize();
    //     cout << "重新申请内存资源" << m_nSize << "字节" << endl;
    //     m_pData = new char[m_nSize];
    //     cout << "复制数据" << m_nSize << "字节" << endl;
    //     memcmp(m_pData, other.GetData(), m_nSize);
    //     return *this;
    // }
    // 可以接收右值引用为参数的赋值操作符
    MemoryBlock &operator=(MemoryBlock &&other)
    {
        // 第一步，释放已有内存资源
        cout << "释放已有资源" << m_nSize << "字节" << endl;
        delete[] m_pData;
        // 第二步，移动资源，也就是移交内存资源的管理权
        cout << "移动资源" << other.m_nSize << "字节" << endl;
        m_pData = other.m_pData;
        m_nSize = other.m_nSize;
        other.m_pData = nullptr;
        other.m_nSize = 0;

        return *this;
    }

public:
    unsigned int GetSize() const
    {
        return m_nSize;
    }
    char *GetData() const
    {
        return m_pData;
    }

private:
    unsigned int m_nSize;
    char *m_pData;
};
MemoryBlock CreateBlock(const unsigned int nSize)
{
    MemoryBlock mem(nSize);
    char *p = mem.GetData();
    memset(mem.GetData(), 'A', mem.GetSize());
    return mem;
}
int main()
{
    MemoryBlock block(256);
    block = CreateBlock(1024);
    cout << "创建的对象大小是" << block.GetSize() << "字节" << endl;
    return 0;
}