# -*- coding: gb18030 -*-
#
# $Id: PetModelRender.py,v 1.5 2008-08-28 03:56:26 huangyongwei Exp $

"""
implement model's ui render

2008.07.31 -- by huangyongwei
"""

from config.client import ItemModel
from guis import *
from guis.controls.AdjModelRender import AdjModelRender
from gbref import rds
import Define

class TalismanModelRender( AdjModelRender ) :
	__cc_config = "config/client/uimodel_configs/talisman.py"

	def __init__( self, mirror ) :
		AdjModelRender.__init__( self, mirror, 0, self.__cc_config )
		self.bgTexture = "guis/general/playerprowindow/talisman/back.dds"
		self.mapping = util.getGuiMapping( ( 512, 512 ), 93, 422, 126, 379 )

	# ----------------------------------------------------------------
	# private
	# ----------------------------------------------------------------
	def __onModelCreated( self, itemModelID, model ) :
		"""
		����ģ�ͻص�
		"""
		if model is None :
			self.cfgKey_ = 0
			# "����ģ��ʧ�ܣ�"
			showMessage( 0x0561, "", MB_OK, pyOwner = self )
		else :
			self.cfgKey_ = itemModelID
			effectIDs = rds.itemModel.getMEffects( itemModelID )
			for effectID in effectIDs:
				dictData = rds.spellEffect.getEffectConfigDict( effectID )
				if len( dictData ) == 0: continue
				effect = rds.skillEffect.createEffect( dictData, model, model, Define.TYPE_PARTICLE_PLAYER,  Define.TYPE_PARTICLE_PLAYER )
				effect.start()
		self.setModel( model )


	# ----------------------------------------------------------------
	# protected
	# ----------------------------------------------------------------
	def onModelChanged_( self, oldModel ) :
		"""
		ģ�͸ı�ʱ������
		"""
		AdjModelRender.onModelChanged_( self, oldModel )
		if self.model : self.model.play()


	# ----------------------------------------------------------------
	# public
	# ----------------------------------------------------------------
	def resetModel( self, itemModelID, bgCreate = True ) :
		"""
		��������ģ��
		@type			itemModelID : INT32
		@param			itemModelID : ģ�Ͷ�Ӧ����Ʒ ID
		@type			bgCreate	: bool
		@param			bgCreate	: �Ƿ��ں�̨����ģ��
		@return					 	: None
		"""
		if itemModelID == self.cfgKey_ :
			return
		elif itemModelID is None :
			self.setModel( None )
			self.cfgKey_ = 0
			# "����ģ�Ͳ����ڣ�"
			showMessage( 0x0562, "", MB_OK, pyOwner = self )
		else :
			if bgCreate :
				rds.itemModel.createModelBG( itemModelID, Functor( self.__onModelCreated, itemModelID ) )
			else :
				model = rds.itemModel.createModel( itemModelID )
				self.__onModelCreated( itemModelID, model )

	# -------------------------------------------------
	def getViewInfos( self ) :
		"""
		��ȡ����ģ����Ϣ
		"""
		keys = self.configDatas_.keys()
		infos = []
		pathPrifx = "talisman/"														# ����ģ��ǰ׺
		for itemModelID, val in ItemModel.Datas.iteritems( ):
			sources = val.get( "model_source1", None )								# ��ȡģ����Դ
			if sources is None : continue											# ��Դ������
			if not len( sources ) : continue
			source = sources[0]
			if not source.startswith( pathPrifx ) : continue						# �Ƿ�����Դ
			viewInfo = self.getViewInfo( itemModelID )
			pos = Math.Vector3( 0, 0, 0 )
			pitch = 0.0
			yaw = 0.0
			if viewInfo :
				pos = viewInfo["position"]
				pitch = viewInfo["pitch"]
				if viewInfo.has_key( "yaw" ):
					yaw = viewInfo["yaw"]
			modelInfo = self.creatModelInfo_( itemModelID, itemModelID, pos, pitch, yaw )
			if itemModelID == self.cfgKey_ :										# �ѵ�ǰģ�ͷŵ���һλ
				infos.insert( 0, modelInfo )
			else :
				infos.append( modelInfo )
			if itemModelID in keys :
				keys.remove( itemModelID )
		assert infos[0].mark == self.cfgKey_, "current model number is not in model list!"
		infos[0].position = self.modelPos
		infos[0].pitch = self.pitch
		for key in keys :															# ɾ����������ģ������
			self.configDatas_.pop( key )
		return infos