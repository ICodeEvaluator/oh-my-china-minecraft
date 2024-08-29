def GetMCPCheckNum(self, mcp, salt):
    import sys
    import mcp_log
    import mod.client.extraClientApi as clientApi
    for path in sys.path_importer_cache.keys():
        if RkvQvzOGnAwSnMiJqGmZMYdzNvwMTZpk.endswith('vanilla.mcp'):
            import binascii
            from common.network import defaultrpc as rpc
            aqTFgnWsqTToNJyzbeELXzjOxpfzAixq = binascii.unhexlify(mcp)
            importer_ins = sys.path_importer_cache[path]
            if getattr(importer_ins, 'read_module', None) is not None:
                dyMCP = sys.path_importer_cache[path].read_module('dynamicMCPLoader', data)
                cISlmwyEXvGgcqkngGEVvtXZfXcpXzQD = gaQuNFPQMiVEfCriJKOqIDexqYIkEoMg.CalcCheckNum(salt + '0')
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl = [(ord(XYRCXwfYrGIhNidUSDbRTWUCpGKgHDKn) * 2 + 5) ^ 255 for XYRCXwfYrGIhNidUSDbRTWUCpGKgHDKn in cISlmwyEXvGgcqkngGEVvtXZfXcpXzQD]
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append('2.12.25.249159') 
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append("android")
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append('2.12.45.252671') 
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append('android')
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append(2)
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append(12)
                VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl.append(clientApi.GetLocalPlayerId())
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz = []
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz.append(False)
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz.append([])
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz.append('')
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz.append('')
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz.append(3)
                liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz.append(gaQuNFPQMiVEfCriJKOqIDexqYIkEoMg.CalcCheckNum(('').join(list(map(str, VKEflxSpJPhKyhYBzZyUwBsAsPGwgpWl)))))
                FBinOTEWhQbWbXNJvnVEtVCtvKeQMuul = cISlmwyEXvGgcqkngGEVvtXZfXcpXzQD[16:]
                for ZpCgaKazjHEPntBrKOUxxVHKaHgIppZg in liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz:
                    FBinOTEWhQbWbXNJvnVEtVCtvKeQMuul += str(ZpCgaKazjHEPntBrKOUxxVHKaHgIppZg)
                FBinOTEWhQbWbXNJvnVEtVCtvKeQMuul += cISlmwyEXvGgcqkngGEVvtXZfXcpXzQD[:16]
                mqWCgDdelFiZAbxMBWFVvitrPOrxVGoG = gaQuNFPQMiVEfCriJKOqIDexqYIkEoMg.CalcCheckNum(FBinOTEWhQbWbXNJvnVEtVCtvKeQMuul)
                rpc.CServerRpc().SetMCPCheckNum([cISlmwyEXvGgcqkngGEVvtXZfXcpXzQD,mqWCgDdelFiZAbxMBWFVvitrPOrxVGoG] + liiMQaFzPTiKAlzoaJWjuqXPWQLORcIz)
    return