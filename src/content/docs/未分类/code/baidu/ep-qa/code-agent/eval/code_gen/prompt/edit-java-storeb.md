---
title: "edit-java-storeb"
description: "你是一个 java 服务端开发工程师，下面是一个商户店铺信息进行新增&修改接口的代码："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\eval\\code_gen\\prompt\\edit-java-storeb.md"
---

你是一个 java 服务端开发工程师，下面是一个商户店铺信息进行新增&修改接口的代码：

## class_method: `com.baidu.pa.storeb.api.shop.StoreShopAgentService.saveOrUpdateMerchant
```java
@APIMethod(read = true, desc = "添加修改店铺")
    CommonSingleResponse<AgentShopResp> saveOrUpdateMerchant(Long userId, Long optId, AgentShopRequest request);
```

## class_method: `com.baidu.pa.storeb.biz.platservice.shop.StoreShopAgentServiceImpl.saveOrUpdateMerchant
```java
    public CommonSingleResponse<AgentShopResp> saveOrUpdateMerchant(Long userId, Long optId, AgentShopRequest request) {

        return super.executeCommonSingle("StoreShopAgentService", "saveOrUpdateMerchant",
                request, new AgentShopValidate(),
                () -> shopAgentHandle.saveOrUpdateMerchant(userId, optId, request));
    }

```

## class_method: `com.baidu.pa.storeb.biz.handle.shop.ShopAgentHandle.saveOrUpdateMerchant
```java
AgentShopResp saveOrUpdateMerchant(Long userId, Long optId, AgentShopRequest request);
```

## class_method: `com.baidu.pa.storeb.biz.handle.shop.impl.ShopAgentHandleImpl.saveOrUpdateMerchant
```java
    public AgentShopResp saveOrUpdateMerchant(Long userId, Long optId, AgentShopRequest request) {
        // 初始化TP服务商代操作相关逻辑
        boolean isPosGroup = initPosGroup(userId);
        if (!isPosGroup) {
            throw new APIException(APIExceptionEnum.MERCHANT_ADD_ERROR);
        }

        AgentShopResp agentShopResp = new AgentShopResp();
        agentShopResp.setUcName(request.getUcName());
        // 注册ucId
        if (Constants.SAVE_TYPE_AUDIT.equals(request.getSaveFlag())
                && (request.getUcId() == null || request.getUcId() == 0)) {
            UcRegistRequest ucRegistRequest = new UcRegistRequest();
            ucRegistRequest.setAccountName(request.getUcName());
            ucRegistRequest.setCustName(request.getCompanyVo().getCompanyName());
            ucRegistRequest.setOpUcId(userId);
            ucRegistRequest.setSecureMobile(request.getSecretPhone());
            List<UcRegistRequest.CustContact> list = new ArrayList<>();
            UcRegistRequest.CustContact custContact = new UcRegistRequest.CustContact();
            custContact.setName(request.getContact());
            custContact.setPhone(request.getContactPhone());
            list.add(custContact);
            ucRegistRequest.setCustContacts(list);
            Long aLong = ucBaseService.ucRegist(ucRegistRequest);
            if (aLong == null) {
                throw new APIException(APIExceptionEnum.MERCHANT_GET_UCID_ERROR);
            }
            request.setUcId(aLong);
            UcBindRequest ucBindRequest = new UcBindRequest();
            ucBindRequest.setUcId(aLong);
            ucBindRequest.setAutoCreate(1);
            ucBindRequest.setQueryType(1);
            UcBindInfo ucBindInfo = ucBindApiService.acquireBindInfo(ucBindRequest);
            if (ucBindInfo != null) {
                request.setPassId(ucBindInfo.getPassId());
            }
            if (Constants.ENV_OFFLINE.equals(env) && CollectionUtils.isNotEmpty(userGroupIds)) {
                try {
                    for (Long groupId : userGroupIds) {
                        ucAuthService.addGroupUsers(AddGroupUsersRequest.builder()
                                .groupId(groupId)
                                .ucIds(Lists.newArrayList(aLong))
                                .build());
                    }
                } catch (Exception e) {
                    log.error("addGroupUsers error.ucId:{}", aLong, e);
                }
            }
            // 添加新商户账号到用户组
            AddGroupUsersByGroupNameEnRequest addGroupUsersRequest = buildAddGroupUsersRequest(userId, aLong);
            ucAuthService.addGroupUsersByGroupNameEn(addGroupUsersRequest);
        }
        agentShopResp.setPassId(request.getPassId());
        agentShopResp.setUcId(request.getUcId());
        // 新增
        if (request.getShopId() == null) {
            // 创建商户
            Long merchantId = atomIdService.getAtomId(AtomIdEnum.SHOP_ID);
            ShopInfo shopInfo = convert2Merchant(request.getUcId(), merchantId, request, null);
            shopInfoDao.insert(shopInfo);
            // 保存地图
            ShopMap shopMap = convert2MerchantMap(shopInfo, request);
            shopMapDao.insertShopMap(shopMap);
            // 保存资质
            ShopTradeQualification shopTradeQualification = convert2Qualify(shopInfo, request);
            if (shopTradeQualification != null) {
                shopTradeQualificationDao.insertSelectiveAndGetId(shopTradeQualification);
            }

            TpUserInfo tpUserInfo = new TpUserInfo();
            tpUserInfo.setTpId(userId);
            BeanUtils.copyProperties(request, tpUserInfo);
            tpUserInfo.setShopId(merchantId);
            tpUserInfoMapper.insertSelective(tpUserInfo);
            agentShopResp.setShopId(merchantId);
            this.insertAuditLog(shopInfo, shopMap);
            return agentShopResp;
        }
        // 更新操作
        ShopInfo merchant = shopInfoDao.findShopInfoById(request.getShopId());
        if (ShopInfoStatusType.SHOP_STATUS_AUDIT.getType() == merchant.getAuditStatus()) {
            throw new APIException(APIExceptionEnum.MERCHANT_ERROR);
        }
        TpUserInfo tpUserInfo = tpUserInfoMapper.selectByPrimaryKey(request.getId());
        if (tpUserInfo.getUcId() == 0) {
            tpUserInfo.setUcId(request.getUcId());
            tpUserInfo.setPassId(request.getPassId());
            tpUserInfo.setContact(request.getContact());
            tpUserInfo.setContactPhone(request.getContactPhone());
            tpUserInfo.setSecretPhone(request.getSecretPhone());
            tpUserInfo.setUcName(request.getUcName());
            tpUserInfoMapper.updateByPrimaryKeySelective(tpUserInfo);
        }
        agentShopResp.setShopId(shopInfo.getId());
        return agentShopResp;
    }

```

#### 可以参考的公共方法：
```java
@Resource
protected ShopInfoDao shopInfoDao;

public void updateByPrimaryKey(ShopInfo updatedShopInfo, Long shopId) {
    ShopInfoExample example = new ShopInfoExample();
    example.createCriteria().andIdEqualTo(shopId);
    shopInfoMapper.updateByExampleSelective(updatedShopInfo, example);
}

@Resource
protected ShopMapDao shopMapDao;

public void updateSelectiveById(ShopMap updatedShopMap) {
    shopMapMapper.updateByPrimaryKeySelective(updatedShopMap);
}

@Resource
protected ShopTradeQualificationDao shopTradeQualificationDao;

public void updateSelectiveById(ShopTradeQualification tradeOnline, Integer id) {
    ShopTradeQualificationExample example = new ShopTradeQualificationExample();
    example.createCriteria().andIdEqualTo(id);
    shopTradeQualificationMapper.updateByExampleSelective(tradeOnline, example);
}

private ShopInfo convert2Merchant(Long userId,
                                  Long shopId,
                                  AgentShopRequest request,
                                  ShopInfo dbShop) {
    Integer auditStatus = Constants.SAVE_TYPE_AUDIT.equals(request.getSaveFlag()) ?
            ShopInfoStatusType.SHOP_STATUS_AUDIT.getType() : ShopInfoStatusType.SHOP_STATUS_DRAFT.getType();

    ShopInfo shopInfo = new ShopInfo();
    if (dbShop != null) {
        BeanUtils.copyProperties(dbShop, shopInfo);
    }
    shopInfo.setId(shopId);
    shopInfo.setUcId(request.getUcId());
    shopInfo.setPassId(request.getPassId());
    shopInfo.setTpId(String.valueOf(userId));
    shopInfo.setAppId(Constants.JMY_APP_ID);
    shopInfo.setSubappId(Constants.SUB_APP_ID_LIFE);
    shopInfo.setIsMaster(Constants.MASTER_SHOP_YES);
    shopInfo.setPoiFlag(Constants.POI_SHOP_NO);
    shopInfo.setExemptType(ShopExemptEnum.NOT_EXEMPT.getId());
    shopInfo.setName(request.getCompanyVo().getCompanyName());
    shopInfo.setCompanyName(request.getCompanyVo().getCompanyName());
    shopInfo.setSource(ShopSourceType.TP.getCode());
    shopInfo.setModFlag(MasterShopModFlag.AGENT_MOD.getCode());
    shopInfo.setAuditStatus(auditStatus);
    return shopInfo;
}
private ShopMap convert2MerchantMap(ShopInfo merchant, AgentShopRequest request) {
    ShopMap dbMap = shopMapDao.getByShopId(merchant.getId());
    ShopMap shopMap = new ShopMap();
    if (dbMap != null) {
        BeanUtils.copyProperties(dbMap, shopMap);
    }

    Integer auditStatus = Constants.SAVE_TYPE_AUDIT.equals(request.getSaveFlag()) ?
            ShopInfoStatusType.SHOP_STATUS_AUDIT.getType() : ShopInfoStatusType.SHOP_STATUS_DRAFT.getType();

    shopMap.setAppId(Constants.JMY_APP_ID);
    shopMap.setSubAppId(Constants.SUB_APP_ID_LIFE);
    shopMap.setShopId(merchant.getId());
    shopMap.setAuditStatus(auditStatus);
    shopMap.setShopName(merchant.getName());
    shopMap.setExemptType(MapExemptEnum.NO_POI_EXEMPT.getId());
    return shopMap;
}

// 此外shopMap和ShopTradeQualification对象都有getId()
// public Integer getId() {
//     return id;
// }
```


请根据上面的接口代码内容，并参考当前项目代码风格和公共方法，根据新增商户部分的逻辑，补全更新商户部分的逻辑，要求：
1. 根据当前请求参数和原始商户信息构建 shopInfo，并更新数据库中已有的商户信息
2. 根据 shopInfo 和 request 构建 shopMap 对象，若 shopMap 有 ID（即已有记录），则更新数据库中的对应记录
3. 根据 shopInfo 和 request 构建商户资质信息，如果资质对象不为空，且已存在记录，则更新数据库中的对应记录
4. 参考新增部分，补充日志记录
请输出你修改的代码：